import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]
        )

    def test_empty_string(self):
        self.assertEqual(markdown_to_blocks(""), [])

    def test_only_newlines(self):
        md = "\n\n\n\n"
        self.assertEqual(markdown_to_blocks(md), [])

    def test_leading_and_trailing_spaces(self):
        md = "  Paragraph 1  \n\n  Paragraph 2\n\n"
        self.assertEqual(markdown_to_blocks(md), ["Paragraph 1", "Paragraph 2"])

    def test_single_block(self):
        md = "This is a single paragraph without double newline."
        self.assertEqual(markdown_to_blocks(md), ["This is a single paragraph without double newline."])

if __name__ == "__main__":
    unittest.main()
