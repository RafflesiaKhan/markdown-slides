# Detailed Guide: How to Use and Update Markdown Slides

This guide provides detailed instructions for reusing and updating the Markdown Slides project. It covers everything from creating new content to deploying changes.

## Table of Contents

1. [Adding New Slide Presentations](#adding-new-slide-presentations)
2. [Updating Existing Slide Content](#updating-existing-slide-content)
3. [Adding New Pages to Documentation](#adding-new-pages-to-documentation) 
4. [Markdown Formatting Guide](#markdown-formatting-guide)
5. [Running and Viewing Changes](#running-and-viewing-changes)
6. [Deployment to GitHub Pages](#deployment-to-github-pages)

## Adding New Slide Presentations

### Step 1: Create a New Markdown File

Create a new `.md` file in the `docs/slides/` directory:

```bash
# Navigate to the slides directory
cd docs/slides/

# Create new markdown file
touch my-new-presentation.md
```

### Step 2: Write Your Slide Content

Open the new file in any text editor and add your slide content using Markdown:

```markdown
# My New Presentation Title

Introduction text for your first slide

---

## Second Slide

- Important point 1
- Important point 2
- Important point 3

---

## Another Slide

More content goes here

---

## Slide with an Image

![Description](https://example.com/image.jpg)
```

### Step 3: Convert to HTML Slides

Run the converter script to generate the HTML presentation:

```bash
# Make sure you're in the project root directory
cd /path/to/markdown-slides

# Convert your new markdown file
python convert_md_to_slides.py docs/slides/my-new-presentation.md
```

### Step 4: Add to Navigation

Edit the `docs/index.md` file to add a link to your new presentation:

```markdown
## Available Presentations

- [Example Presentation](slides/presentations/example.html)
- [How to Create Slides](slides/presentations/how-to-create.html)
- [My New Presentation](slides/presentations/my-new-presentation.html)
```

## Updating Existing Slide Content

### Step 1: Edit the Markdown File

1. Find the markdown file you want to update in the `docs/slides/` directory
2. Open it in your text editor
3. Make your changes to the content
4. Save the file

### Step 2: Regenerate the HTML

After making changes, regenerate the HTML slides:

```bash
# Regenerate a single presentation
python convert_md_to_slides.py docs/slides/the-file-you-edited.md

# Or regenerate all presentations
python convert_md_to_slides.py docs/slides
```

## Adding New Pages to Documentation

### Step 1: Create a New Markdown File

Create a new `.md` file in the `docs/` directory:

```bash
# Create a new documentation page
touch docs/new-page.md
```

### Step 2: Add Content to the Page

Write your page content using Markdown:

```markdown
# New Page Title

This is a new documentation page.

## First Section

Content for the first section goes here.

## Second Section

Content for the second section goes here.
```

### Step 3: Update MkDocs Configuration

Edit the `mkdocs.yml` file to add your new page to the navigation:

```yaml
# Find the nav section and add your page
nav:
  - Home: index.md
  - Slides:
    - Example Presentation: slides/example.md
    - How to Create Slides: slides/how-to-create.md
  - About: about.md
  - New Page: new-page.md  # Add this line
```

## Markdown Formatting Guide

### Basic Text Formatting

```markdown
# Heading 1
## Heading 2
### Heading 3

*Italic text*
**Bold text**
***Bold and italic***
~~Strikethrough~~

> Blockquote text
```

### Lists

```markdown
# Unordered Lists
- Item 1
- Item 2
  - Nested item 2.1
  - Nested item 2.2
- Item 3

# Ordered Lists
1. First item
2. Second item
   1. Nested item 2.1
   2. Nested item 2.2
3. Third item
```

### Links and Images

```markdown
# Link
[Link text](https://example.com)

# Image
![Alt text](image.jpg)

# Image with size (HTML works in Markdown)
<img src="image.jpg" width="300" height="200">
```

### Code Blocks

````markdown
# Inline code
Use `code` in a sentence

# Code block
```python
def hello_world():
    print("Hello, World!")
```

# Code block with line numbers
```python linenums="1"
def hello_world():
    print("Hello, World!")
```
````

### Tables

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

## Running and Viewing Changes

### Start the MkDocs Server

```bash
# Activate the virtual environment (if not already active)
source .markdown-slides/bin/activate

# Start MkDocs server on default port
mkdocs serve

# Or specify a custom port
mkdocs serve -a 127.0.0.1:8087
```

### View in Browser

Open your web browser and navigate to:
- http://127.0.0.1:8000 (default port)
- or http://127.0.0.1:8087 (custom port)

### Presentation Controls

When viewing a slide presentation:
- Use **right/left arrow** keys to navigate between horizontal slides
- Use **up/down arrow** keys to navigate between vertical slides
- Press **ESC** to see an overview of all slides
- Press **F** to enter fullscreen mode
- Press **S** to see speaker notes (if added)

## Deployment to GitHub Pages

### Step 1: Commit Your Changes

```bash
# Add all changes
git add .

# Commit with a meaningful message
git commit -m "Add new presentation and update documentation"

# Push to GitHub
git push origin main
```

### Step 2: Deploy with MkDocs

```bash
# Build and deploy to GitHub Pages
mkdocs gh-deploy
```

### Step 3: Access Your Published Site

Your site will be available at:
```
https://yourusername.github.io/repository-name/
```

## Troubleshooting

### Slides Not Showing Properly
- Make sure you've run the converter script after making changes
- Check that your Markdown syntax is correct
- Ensure horizontal dividers use `---` on a line by themselves
- Verify vertical dividers use `--` on a line by themselves

### MkDocs Server Issues
- Check that you've activated the virtual environment
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Try stopping and restarting the server
- Check for port conflicts if using a custom port
