import unittest
from textnode import TextNode, TextType
from split_nodes_delim import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_single_inline_code(self):
        input_nodes = [TextNode("Here is `code`.", TextType.TEXT)]
        result = split_nodes_delimiter(input_nodes, "`", TextType.CODE)
        expected = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_multiple_inline_bold(self):
        input_nodes = [TextNode("**bold** and more **bold**!", TextType.TEXT)]
        result = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" and more ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("!", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_mixed_non_text_nodes_unchanged(self):
        input_nodes = [
            TextNode("**bold**", TextType.TEXT),
            TextNode("unchanged", TextType.CODE)
        ]
        result = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)
        self.assertEqual(result[-1], TextNode("unchanged", TextType.CODE))

    def test_uneven_delimiters_raises(self):
        input_nodes = [TextNode("This is `broken.", TextType.TEXT)]
        with self.assertRaises(Exception) as cm:
            split_nodes_delimiter(input_nodes, "`", TextType.CODE)
        self.assertIn("Unmatched delimiter", str(cm.exception))

    def test_italic_underscore_split(self):
        input_nodes = [TextNode("This _is_ cool", TextType.TEXT)]
        result = split_nodes_delimiter(input_nodes, "_", TextType.ITALIC)
        expected = [
            TextNode("This ", TextType.TEXT),
            TextNode("is", TextType.ITALIC),
            TextNode(" cool", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
