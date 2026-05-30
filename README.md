# originaljcblog
Tech blog page using a custom static site generator

Markdown files in `content/` support YAML frontmatter with `title`, `date`, and an optional `published` flag.

Set `published: false` to keep a draft post in `content/` without generating it into `dist/`.

Usage
docker build -t originaljcblog .
docker run --rm -v "$(Get-Location)\dist:/app/dist" originaljcblog