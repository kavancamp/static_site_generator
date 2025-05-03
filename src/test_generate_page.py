import unittest
from pathlib import Path
import tempfile
from generate_page import generate_page

class TestGeneratePage(unittest.TestCase):
    def test_generate_page_output(self):
        md_content = "# Hello\nThis is a test paragraph."
        template_content = "<html><body>{{ content }}</body></html>"

        with tempfile.TemporaryDirectory() as temp_dir:
            from_path = Path(temp_dir) / "input.md"
            template_path = Path(temp_dir) / "template.html"
            dest_path = Path(temp_dir) / "output.html"

            from_path.write_text(md_content)
            template_path.write_text(template_content)

            generate_page(from_path, template_path, dest_path)

            result = dest_path.read_text()
            self.assertIn("<h1>Hello</h1>", result)
            self.assertIn("<p>This is a test paragraph.</p>", result)
            self.assertTrue(result.startswith("<html>"))

if __name__ == "__main__":
    unittest.main()
