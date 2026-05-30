import shutil
import markdown
import yaml
from pathlib import Path
from datetime import datetime

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


def format_date(value):
    if not value:
        return ""
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, str):
        try:
            normalized = value.rstrip("Z")
            return datetime.fromisoformat(normalized).date().isoformat()
        except ValueError:
            return value.split()[0]
    return str(value)


def is_published(metadata):
    value = metadata.get("published", True)
    if isinstance(value, str):
        return value.strip().lower() not in ("false", "no", "0", "off")
    return bool(value)


# -------------------------------------------------------------------
# Build
# -------------------------------------------------------------------
def clear_output_dir():
    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        return

    for child in OUTPUT_DIR.iterdir():
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()


def build_site():
    # Clean dist/
    clear_output_dir()

    posts = []

    # Process Markdown files into HTML pages
    for md_file in CONTENT_DIR.glob("*.md"):
        raw_text = md_file.read_text(encoding="utf-8")
        metadata, body = parse_frontmatter(raw_text)

        if not is_published(metadata):
            continue

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
        display_date = format_date(post["date"])
        index_content += f'<li><a href="{post["file"]}">{post["title"]}</a> {display_date}</li>'
    index_content += "</ul>"

    index_html = render_page("The Original JC", index_content)
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")

    # Copy static files
    if STATIC_DIR.exists():
        shutil.copytree(STATIC_DIR, OUTPUT_DIR / "static", dirs_exist_ok=True)

    print("Site built into dist/")

if __name__ == "__main__":
    build_site()
