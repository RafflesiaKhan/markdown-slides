# Simple Markdown Slides

A straightforward system for creating beautiful presentations from Markdown files without needing JavaScript knowledge.

## Features

- Write slides in simple Markdown
- Presentations display beautifully using Reveal.js
- Documentation website with MkDocs
- No JavaScript coding required
- Automatic deployment to GitHub Pages

## How It Works

1. **Write content in Markdown** - Create `.md` files with your slide content
2. **Convert to HTML slides** - Use the simple Python converter tool
3. **View in browser** - See beautiful presentations with navigation controls

## Getting Started

### Creating a Virtual Environment

It is recommended to use a Python virtual environment to manage dependencies for this project. To create and activate a virtual environment, run:

```bash
# Create a virtual environment named .markdown-slides
python3 -m venv .markdown-slides

# Activate the virtual environment (on macOS/Linux)
source .markdown-slides/bin/activate

# On Windows, use:
.markdown-slides\Scripts\activate
```

### Installation

```bash
# Activate the virtual environment
source .markdown-slides/bin/activate

# Install requirements if needed
pip install -r requirements.txt
```

### Creating Slides

1. **Create a Markdown file** in the `docs/slides/` directory
2. **Format your content** with standard Markdown
3. **Separate slides** with:
   - `---` for horizontal slides (new slide to the right)
   - `--` for vertical slides (new slide below)

**Example:**

```markdown
# My Presentation

## First Slide
- Point 1
- Point 2

---

## Second Slide
More content here

---

## Vertical Slides
This slide has sub-slides

--

### Sub-slide 1
Navigate down to see me
```

### Converting to HTML Slides

Use the simple converter tool to turn your Markdown into presentations:

```bash
# Convert a single file
python convert_md_to_slides.py docs/slides/your-slide.md

# Convert all markdown files in the slides directory
python convert_md_to_slides.py docs/slides
```

### Viewing Your Slides

Start the MkDocs server:

```bash
# Start on default port 8000
mkdocs serve

# Or specify a different port
mkdocs serve -a 127.0.0.1:8087
```

Visit http://localhost:8000 (or your chosen port) and click on the slide links.

## Project Structure

```
mkdocs.yml               # MkDocs configuration
docs/
  index.md               # Home page with links to slides
  about.md               # About page
  slides/                # Your Markdown slide files
    example.md           # Example presentation in Markdown
    how-to-create.md     # Tutorial on creating slides
    presentations/       # Generated HTML presentations
      example.html       # HTML version of example.md
      how-to-create.html # HTML version of how-to-create.md
convert_md_to_slides.py  # Converter tool
requirements.txt         # Python dependencies
```

## Deploying to GitHub Pages

1. Push this repository to GitHub
2. Enable GitHub Pages in repository settings
3. Your slides will be available at `https://yourusername.github.io/repository-name/`

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Reveal.js Documentation](https://revealjs.com/)
- [Markdown Guide](https://www.markdownguide.org/)

# Demo

[Demo.mov](Demo.mov)