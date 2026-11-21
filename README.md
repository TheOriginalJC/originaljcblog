# originaljcblog
Tech blog page using a custom static site generator

Markdown files in `content/` support YAML frontmatter with `title`, `date`, and an optional `published` flag.

Set `published: false` to keep a draft post in `content/` without generating it into `dist/`.

Dependencies are controlled manually in `requirements.in`. After changing versions there, regenerate the hash-locked `requirements.txt` with:

```powershell
pip-compile --generate-hashes --output-file=requirements.txt requirements.in
```

Docker and GitHub Actions install from `requirements.txt`. No scheduled dependency updates are configured.

Usage
docker build -t originaljcblog .
docker run --rm -v "$(Get-Location)\dist:/app/dist" originaljcblog