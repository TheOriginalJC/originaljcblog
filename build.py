import shutil
import markdown
import yaml
from pathlib import Path

CONTENT_DIR = Path("content")
OUTPUT_DIR = Path("dist")
TEMPLATES_DIR = Path("templates")
STATIC_DIR = Path("static")

# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------
def parse_frontmatter(md_text):
    """
    Splits YAML frontmatter (between --- lines) from the body.
    Returns (metadata_dict, body_text).
    """
    if md_text.startswith("---"):
        _, fm, body = md_text.split("---", 2)
        metadata = yaml.safe_load(fm) or {}
        return metadata, body.strip()
    return {}, md_text

def render_page(title, content_html):
    """
    Wraps HTML content with header + footer templates.
    Replaces {{ title }} in header.html with the page title.
    """
    header = (TEMPLATES_DIR / "header.html").read_text(encoding="utf-8")
    footer = (TEMPLATES_DIR / "footer.html").read_text(encoding="utf-8")

    header = header.replace("{{ title }}", title)

    return f"{header}\n{content_html}\n{footer}"

def adjust_image_paths(html: str) -> str:
    # Prepend "static/" if the path doesn’t already start with http or static/
    return html.replace('src="', 'src="static/')


# -------------------------------------------------------------------
# Build
# -------------------------------------------------------------------
def build_site():
    # Clean dist/
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    posts = []

    # Process Markdown files into HTML pages
    for md_file in CONTENT_DIR.glob("*.md"):
        raw_text = md_file.read_text(encoding="utf-8")
        metadata, body = parse_frontmatter(raw_text)

        html_body = markdown.markdown(body)
        html_body = adjust_image_paths(html_body)
        title = metadata.get("title", "Untitled")

        page_html = render_page(title, html_body)

        output_file = OUTPUT_DIR / f"{md_file.stem}.html"
        output_file.write_text(page_html, encoding="utf-8")

        posts.append({"title": title, "file": f"{md_file.stem}.html", "date": metadata.get("date", "")})

    # Build index.html
    posts.sort(key=lambda x: x["date"], reverse=True)
    index_content = "<h2>Posts</h2>\n<ul>"
    for post in posts:
        index_content += f'<li><a href="{post["file"]}">{post["title"]}</a> {post["date"]}</li>'
    index_content += "</ul>"

    index_html = render_page("The Original JC", index_content)
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")

    # Copy static files
    if STATIC_DIR.exists():
        shutil.copytree(STATIC_DIR, OUTPUT_DIR / "static", dirs_exist_ok=True)

    print("Site built into dist/")

if __name__ == "__main__":
    build_site()
