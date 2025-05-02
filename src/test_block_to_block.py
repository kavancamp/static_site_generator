import unittest
from markdown_to_blocks import block_to_block_type, BlockType

class TestBlockTypeDetection(unittest.TestCase):

    def test_heading(self):
        block = "# Heading text"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_code_block(self):
        block = "```\ndef func():\n    return True\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        block = "> This is a quote\n> More quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- item one\n- item two\n- item three"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. first item\n2. second item\n3. third item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        block = "This is a regular paragraph of text."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_mixed_unordered_list_fails(self):
        block = "- item one\nnot a list item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_incorrect_ordered_numbers(self):
        block = "1. item\n3. wrong number"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
