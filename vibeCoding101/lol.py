# ...existing code...
# Extract and summarize "Assessment Methods" from the syllabus in Course_Docs/
from pathlib import Path
import re, sys

def find_syllabus_files(course_docs: Path):
    md_txt = []
    others = []
    if not course_docs.exists():
        return md_txt, others
    for f in course_docs.rglob('*'):
        if not f.is_file():
            continue
        name = f.name.lower()
        if 'syllabus' in name or 'course outline' in name or 'gcap' in name:
            if f.suffix.lower() in {'.md', '.txt'}:
                md_txt.append(f)
            else:
                others.append(f)
    # Fallback: any MD that mentions "assessment"
    if not md_txt:
        for f in course_docs.rglob('*.md'):
            try:
                if 'assessment' in f.read_text(encoding='utf-8', errors='ignore').lower():
                    md_txt.append(f)
            except Exception:
                pass
    return md_txt, others

def extract_assessment_section(text: str):
    # Capture from a heading that includes "Assessment" up to the next heading
    patterns = [
        r'(?is)(^#{1,6}.*assessment.*?$)(.*?)(?=^#{1,6}\s|\Z)',   # Markdown headings
        r'(?is)(^\d+\.\s*assessment.*?$)(.*?)(?=^\d+\.\s|\Z)',    # Numbered heading
        r'(?is)(^assessment(?: methods| and evaluation|)\s*$)(.*?)(?=^\S|\Z)'  # Plain heading line
    ]
    for pat in patterns:
        m = re.search(pat, text, flags=re.M)
        if m:
            return (m.group(1) + "\n" + m.group(2)).strip()
    # Fallback: collect bullets containing assessment info
    lines = text.splitlines()
    hits = [ln for ln in lines if re.search(r'assessment', ln, re.I)]
    if hits:
        idxs = [lines.index(hits[0])]
        start = max(0, idxs[0] - 3)
        end = min(len(lines), idxs[0] + 60)
        return "\n".join(lines[start:end]).strip()
    return ""

def summarize_assessment(md: str):
    bullets = []
    for ln in md.splitlines():
        if re.match(r'^\s*([-*]|\d+[\.\)])\s+', ln):
            bullets.append(ln.strip())
    items = []
    for b in bullets:
        # Try to extract weight and name
        m1 = re.search(r'(?P<name>.*?)(?:[-–—:]\s*)?(?P<pct>\d{1,3})\s*%', b)
        m2 = re.search(r'(?P<pct>\d{1,3})\s*%\s*(?P<name>.+)', b)
        name, pct = None, None
        if m1:
            name = m1.group('name').strip(' -–—:').strip()
            pct = m1.group('pct')
        elif m2:
            name = m2.group('name').strip()
            pct = m2.group('pct')
        else:
            # Clean bullet marker
            name = re.sub(r'^\s*([-*]|\d+[\.\)])\s*', '', b).strip()
        items.append((name, pct))
    # Build concise summary text
    lines = []
    total = 0
    for name, pct in items:
        if pct:
            total += int(pct)
            lines.append(f"- {name} — {pct}%")
        else:
            lines.append(f"- {name}")
    if total:
        lines.append(f"- Total weight accounted: {total}%")
    return "\n".join(lines) if lines else "No bullet-pointed assessment items found."

# Resolve Course_Docs from the notebook folder (cwd should be vibeCoding101)
nb_root = Path.cwd()
candidates = [nb_root.parent / "Course_Docs", nb_root / "Course_Docs"]
course_docs = next((p for p in candidates if p.exists()), None)

if not course_docs:
    print("Course_Docs/ folder not found next to vibeCoding101/. Please confirm its location.")
else:
    md_txt_files, other_files = find_syllabus_files(course_docs)
    if not md_txt_files and other_files:
        print("Found syllabus files but not in .md/.txt format (e.g., PDF/DOCX). Please open/convert one of these:")
        for f in other_files:
            print(f" - {f}")
    elif not md_txt_files:
        print("No syllabus .md/.txt found in Course_Docs/.")
    else:
        # Use the first candidate
        syllabus_path = md_txt_files[0]
        content = syllabus_path.read_text(encoding='utf-8', errors='ignore')
        section = extract_assessment_section(content)
        if not section:
            print(f"Assessment section not found in {syllabus_path}.")
        else:
            print(f"=== Assessment Methods (source: {syllabus_path.name}) ===\n")
            print(section)
            summary = summarize_assessment(section)
            print("\n---\nConcise Summary:\n")
            print(summary)
            # Save summary
            out_dir = nb_root / "Part1ReadingEditingFiles"
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / "assessment_methods_summary.md"
            out_path.write_text(
                f"# Assessment Methods Summary\n\nSource: {syllabus_path}\n\n## Extracted Section\n\n{section}\n\n## Concise Summary\n\n{summary}\n",
                encoding='utf-8'
            )
            print(f"\nSaved summary to: {out_path}")
# ...existing code...