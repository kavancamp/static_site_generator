import re
import os
from pathlib import Path
from markdown_to_htmlnode import markdown_to_html_node


def extract_title(markdown):
    for line in markdown.splitlines():
        if re.match(r"#(?!#)", line.strip()):
            print(line.lstrip("#").strip())
            return line.lstrip("#").strip()
    raise Exception("No h1 header present")
 

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown and template files
    markdown_content = Path(from_path).read_text()
    template_content = Path(template_path).read_text()

    # Convert markdown to HTML
    html_content = markdown_to_html_node(markdown_content).to_html()

    # Extract the title from markdown
    title = extract_title(markdown_content)

    # Replace placeholders in the template
    final_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    # destination directory exists?
    dest_path = Path(dest_path)
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    # Write the final HTML to the destination file
    dest_path.write_text(final_content)
    
    


