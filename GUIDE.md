# Simple Markdown Slides Guide

This is a simplified system for creating beautiful slide presentations using Markdown without needing to know JavaScript.

## How It Works

1. You write content in regular Markdown files (.md)
2. Run the simple Python script to convert them to slide presentations
3. View the documentation and slides using MkDocs

## Getting Started

### 1. Setup (One-time)

Make sure Python and MkDocs are installed:

```bash
# Activate the virtual environment
source .markdown-slides/bin/activate

# Check if MkDocs is installed
mkdocs --version
```

### 2. Creating Slides

1. Create a Markdown file in the `docs/slides/` directory
2. Format your slides using simple Markdown with slide separators:
   - Use `---` for horizontal slide breaks
   - Use `--` for vertical slide breaks
3. Start with a title heading (# Your Title)

**Example Slide Content:**

```markdown
# My Presentation Title

## First Slide

Content for the first slide

---

## Second Slide

- Bullet point 1
- Bullet point 2

---

## Slide with Code

```python
def hello():
    print("Hello World")
```
```

### 3. Converting to Slides

Run the converter script to turn your Markdown into presentations:

```bash
# Convert a single markdown file
./create_slides.py docs/slides/your-file.md

# Convert all markdown files in a directory
./create_slides.py docs/slides/
```

The HTML slides will be generated in the `docs/slides/presentations/` directory.

### 4. Updating Documentation

To show links to your presentations in the documentation:

1. Edit `docs/index.md` to link to your new slide:

```markdown
- [Your New Presentation](slides/presentations/your-file.html)
```

### 5. Viewing the Site

Start the MkDocs server:

```bash
mkdocs serve -a 127.0.0.1:8087
```

Visit http://127.0.0.1:8087 in your browser to see the documentation and access your slides.

## Slide Controls

When viewing a presentation:
- Use **right/left arrow keys** to navigate between slides
- Use **up/down arrow keys** for vertical slides
- Press **ESC** to see an overview of all slides
- Press **F** to enter fullscreen mode

## Deploying to GitHub Pages

When you're ready to publish your slides:

```bash
mkdocs gh-deploy
```

This will build the site and publish it to GitHub Pages.
