import sys
from pathlib import Path
from generate_page import generate_page
from shutil import rmtree, copy2

def delete_docs_dir():
    docs_dir = Path("docs")
    if docs_dir.exists() and docs_dir.is_dir():
        rmtree(docs_dir)
        print("Deleted existing public/ directory")
        
def copy_static_to_docs(static_dir="static", docs_dir="docs"):
    static_dir = Path(static_dir)
    docs_dir = Path(docs_dir)

    for path in static_dir.rglob("*"):
        relative_path = path.relative_to(static_dir)
        dest_path = docs_dir / relative_path

        if path.is_dir():
            dest_path.mkdir(parents=True, exist_ok=True)
        else:
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            copy2(path, dest_path)
            print(f"Copied {path} to {dest_path}")
            
def generate_all_pages(content_dir="content", template_path="template.html", output_dir="docs", base_path="/"):
    content_dir = Path(content_dir)
    template_path = Path(template_path)
    output_dir = Path(output_dir)

    for path in content_dir.rglob("*.md"):
        relative_path = path.relative_to(content_dir)
        output_path = output_dir / relative_path.with_suffix(".html")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        print(f"Generating {output_path} from {path}")
        generate_page(path, template_path, output_path, base_path)
        
def copy_content_assets(content_dir="content", docs_dir="docs"):
    content_dir = Path(content_dir)
    docs_dir = Path(docs_dir)

    for path in content_dir.rglob("*"):
        if path.suffix.lower() in [".jpg", ".png", ".jpeg", ".gif"]:
            relative_path = path.relative_to(content_dir)
            dest_path = docs_dir / relative_path
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            copy2(path, dest_path)
            print(f"Copied image asset {path} to {dest_path}")
            
def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    delete_docs_dir()
    copy_content_assets()
    copy_static_to_docs()
    generate_all_pages(base_path=base_path)
    
if __name__ == "__main__":
    main()
