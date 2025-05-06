import re
from pathlib import Path
from markdown_to_htmlnode import markdown_to_html_node

def extract_title(markdown):
    for line in markdown.splitlines():
        if re.match(r"#(?!#)", line.strip()):
            return line.lstrip("#").strip()
    raise Exception("No h1 header present")

def generate_page(from_path: Path, template_path: Path, dest_path: Path, base_path="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if not base_path.endswith("/"):
        base_path += "/"
        
    markdown_content = from_path.read_text()
    template_content = template_path.read_text()

    # Convert markdown to HTML and extract title
    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    # Fill template
    final_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    final_content = re.sub(r'href="/(.*?)"', fr'href="{base_path}\1"', final_content)
    final_content = re.sub(r'src="/(.*?)"', fr'src="{base_path}\1"', final_content)
    # Make sure destination directory exists
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    # Write the output HTML file
    dest_path.write_text(final_content)
    print(f"Wrote HTML to {dest_path}")

    


