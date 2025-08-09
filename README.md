# Static Site Generator

This project is a lightweight static site generator written in Python. It converts Markdown files into HTML using a custom template and builds the output into the `docs/` directory, ready to deploy with GitHub Pages.

## 🚀 How to Use

1. Clone the repository:
   bash
  <pre>
   git clone https://github.com/kavancamp/static_site_generator.git
   cd static_site_generator
  </pre>
2. Add your static/content
3. Deploy:
   <pre>
   -Run `python build.sh` to build the site into docs/
   -Push your changes to the main branch
   -GitHub Pages will automatically serve from /docs
   </pre>
4. Visit Site:
   <pre>
   https://kavancamp.github.io/static_site_generator/
   </pre>
⚙️ GitHub Pages Deployment
This project is configured to deploy from the docs/ directory on the main branch using GitHub Pages.

## 📁 Project Structure
<pre>
static_site_generator/
.
├── build.sh              # Bash script to build the site
├── main.sh               # Optional main entry script
├── test.sh               # Test runner script
├── README.md             # Project documentation
├── template.html         # HTML template for generated pages

├── content/              # Markdown source content
│   ├── blog/
│   │   ├── glorfindel/index.md
│   │   ├── majesty/index.md
│   │   └── tom/index.md
│   ├── contact/index.md
│   └── index.md

├── docs/                 # Output folder (generated HTML for GitHub Pages)
│   ├── blog/
│   │   ├── glorfindel/index.html
│   │   ├── majesty/index.html
│   │   └── tom/index.html
│   ├── contact/index.html
│   ├── images/
│   │   ├── glorfindel.png
│   │   ├── rivendell.png
│   │   ├── tolkien.png
│   │   └── tom.png
│   ├── index.css
│   └── index.html

├── static/               # Static files to copy over (CSS, images, etc.)
│   ├── index.css
│   └── images/
├── src/                  # Python source code
│   ├── main.py
│   ├── generate_page.py
│   ├── extract_markdown.py
│   ├── markdown_to_blocks.py
│   ├── markdown_to_htmlnode.py
│   ├── htmlnode.py
│   ├── leafnode.py
│   ├── parentnode.py
│   ├── split_nodes_delim.py
│   ├── text_to_textnode.py
│   ├── textnode.py
│   ├── test_*.py         # Unit tests for each module
│   └── __pycache__/      # Compiled Python bytecode (ignored)
</pre>

🛠 Requirements
Python 3.6+
