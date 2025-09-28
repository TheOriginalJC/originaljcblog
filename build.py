import os
import shutil
import markdown
import yaml
from pathlib import Path

# Paths
CONTENT_DIR = Path("content")
OUTPUT_DIR = Path("dist")
TEMPLATE_DIR = Path("templates")
STATIC_DIR = Path("static")

# Load header and footer templates
header = (TEMPLATE_DIR / "header.html").read_text()
footer = (TEMPLATE_DIR / "footer.html").read_text()

# Clean output folder
if OUTPUT_DIR.exists():
    shutil.rmtree(OUTPUT_DIR)
OUTPUT_DIR.mkdir()

# Copy static assets into site root
if STATIC_DIR.exists():
    print("Copying static assets...")
    for item in STATIC_DIR.iterdir():
        dest = OUTPUT_DIR / item.name
        if item.is_dir():
            shutil.copytree(item, dest, dirs_exist_ok=True)
        else:
            shutil.copy2(item, dest)

# Helper: parse frontmatter (YAML between ---)
def parse_frontmatter(md_text):
    if md_text.startswith("---"):
        _, fm, body = md_text.split("---", 2)
        metadata = yaml.safe_load(fm)
        return metadata, body.strip()
    return {}, md_text

# Build index
index_links = []

for md_file in CONTENT_DIR.glob("*.md"):
    raw_text = md_file.read_text(encoding="utf-8")

    # Extract frontmatter + body
    metadata, body = parse_frontmatter(raw_text)
    html_content = markdown.markdown(body)

    title = metadata.get("title", md_file.stem.title())
    date = metadata.get("date", "")

    # Wrap with header/footer
    page_html = f"{header}\n<h1>{title}</h1>\n{html_content}\n{footer}"

    # Output filename
    out_file = OUTPUT_DIR / f"{md_file.stem}.html"
    out_file.write_text(page_html, encoding="utf-8")

    # Add to index
    index_links.append(
        f'<li><a href="{out_file.name}">{title}</a> {date}</li>'
    )

# Write index.html
index_html = f"{header}\n<h1>Posts</h1>\n<ul>{''.join(index_links)}</ul>\n{footer}"
(OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")

print("Site built in 'dist/' folder")
