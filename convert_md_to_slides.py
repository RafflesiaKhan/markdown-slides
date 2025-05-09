#!/usr/bin/env python3
"""
Simple Markdown to Reveal.js Slides Converter
No JavaScript knowledge required to use this tool
"""

import os
import re
import sys
from pathlib import Path


def extract_title(content):
    """Extract title from the first heading in the markdown file"""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1)
    return "Slide Presentation"


def convert_markdown_to_slides(markdown_file, output_dir="docs/slides/presentations"):
    """Convert a markdown file to a Reveal.js HTML presentation"""
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read markdown content
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get the title from the first heading
    title = extract_title(content)
    
    # Create HTML file with the same name but .html extension
    md_path = Path(markdown_file)
    html_file = Path(output_dir) / f"{md_path.stem}.html"
    
    # Basic HTML with Reveal.js
    html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/dist/reveal.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/dist/theme/white.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/plugin/highlight/monokai.css">
  <style>
    .reveal .slides {{ text-align: left; }}
    .reveal h1, .reveal h2, .reveal h3 {{ color: #2a76dd; }}
    .reveal pre {{ width: 100%; box-sizing: border-box; }}
    .reveal pre code {{ max-height: 500px; padding: 10px; }}
    .back-button {{
      position: fixed;
      top: 10px;
      left: 10px;
      z-index: 1000;
      padding: 8px 15px;
      background: #2a76dd;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
    }}
    .back-button:hover {{ background: #1a66cd; }}
  </style>
</head>
<body>
  <a href="../.." class="back-button">Back to Docs</a>
  
  <div class="reveal">
    <div class="slides">
      <section data-markdown data-separator="^\\n---\\n$" data-separator-vertical="^\\n--\\n$">
        <textarea data-template>
{content}
        </textarea>
      </section>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/dist/reveal.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/plugin/markdown/markdown.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/plugin/highlight/highlight.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/plugin/notes/notes.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/plugin/zoom/zoom.js"></script>
  <script>
    Reveal.initialize({{
      hash: true,
      plugins: [ RevealMarkdown, RevealHighlight, RevealNotes, RevealZoom ]
    }});
  </script>
</body>
</html>
"""
    
    # Write the HTML file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Created: {html_file}")
    return True


def main():
    """Process command line arguments and convert files"""
    # Simple argument handling
    if len(sys.argv) < 2:
        print("Usage: python convert_md_to_slides.py <markdown_file_or_directory>")
        return 1
    
    input_path = sys.argv[1]
    path = Path(input_path)
    
    # Default output directory
    output_dir = "docs/slides/presentations"
    
    # Convert all markdown files in directory
    if path.is_dir():
        print(f"Converting all markdown files in '{input_path}'...")
        files_converted = 0
        
        # Process all markdown files in the directory
        for md_file in path.glob("*.md"):
            if convert_markdown_to_slides(md_file, output_dir):
                files_converted += 1
        
        print(f"Converted {files_converted} files to HTML slide presentations.")
        return 0 if files_converted > 0 else 1
    
    # Convert single file
    elif path.is_file() and path.suffix.lower() == '.md':
        return 0 if convert_markdown_to_slides(path, output_dir) else 1
    
    else:
        print(f"Error: '{input_path}' is not a markdown file or directory.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
