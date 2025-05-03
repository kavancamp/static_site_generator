import os
import re
from pathlib import Path

from generate_page import generate_page
from shutil import rmtree, copy2

def delete_public_dir():
    public_dir = Path("public")
    if public_dir.exists() and public_dir.is_dir():
        rmtree(public_dir)
        print("Deleted existing public/ directory")

def copy_static_to_public(static_dir="static", public_dir="public"):
    static_dir = Path(static_dir)
    public_dir = Path(public_dir)

    for path in static_dir.rglob("*"):
        relative_path = path.relative_to(static_dir)
        dest_path = public_dir / relative_path

        if path.is_dir():
            dest_path.mkdir(parents=True, exist_ok=True)
        else:
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            copy2(path, dest_path)
            print(f"Copied {path} to {dest_path}")

def main():
    delete_public_dir()
    copy_static_to_public()

    generate_page(
        from_path=Path("content/index.md"),
        template_path=Path("template.html"),
        dest_path=Path("public/index.html")
    )

if __name__ == "__main__":
    main()
