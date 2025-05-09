# How to Create Slides

<!-- .slide: data-separator="^\n---\n$" data-separator-vertical="^\n--\n$" -->

## Creating Your Own Slides

A step-by-step guide to creating presentations with Markdown

---

## Step 1: Create a Markdown File

- Add a new `.md` file in the `docs/slides/` folder
- Start with a top-level heading for the title
- Add the slide configuration comment:

```markdown
<!-- .slide: data-separator="^\n---\n$" data-separator-vertical="^\n--\n$" -->
```

---

## Step 2: Structure Your Content

- Use `---` to separate horizontal slides
- Use `--` to create vertical slides
- Each slide typically starts with a heading

---

## Step 3: Format Your Content

### Headings

```markdown
# Heading 1
## Heading 2
### Heading 3
```

---

## Lists and Text

Bulleted lists:
```markdown
- Item 1
- Item 2
  - Nested item
```

Numbered lists:
```markdown
1. First step
2. Second step
```

---

## Formatting Text

```markdown
**Bold text**
*Italic text*
~~Strikethrough~~
> Blockquote
`Inline code`
```

---

## Code Blocks

```markdown
```python
def hello_world():
    print("Hello, World!")
```
```

---

## Images

```markdown
![Alt text](path/to/image.jpg)
```

For responsive images:

```markdown
<img src="path/to/image.jpg" style="max-width:80%;">
```

---

## Links

```markdown
[Link text](https://example.com)
```

Internal links:

```markdown
[Go to another slide](another-slide.md)
```

---

## Step 4: Add to Navigation

Edit `mkdocs.yml` to add your new slide:

```yaml
nav:
  - Home: index.md
  - Slides:
    - Your New Slide: slides/your-file-name.md
```

---

## Step 5: View Your Presentation

- Run `mkdocs serve` 
- Go to `/slides/your-file-name.html`
- Use arrow keys to navigate

---

## Advanced Features

- Fragments (revealed one by one)
- Speaker notes
- Custom backgrounds
- Transitions

Check Reveal.js documentation for more!

---

## That's It!

Now you're ready to create amazing presentations with Markdown
