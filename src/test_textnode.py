import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2, "TextNodes with same text and type should be equal")

    def test_textnode_inequality_text(self):
        node = TextNode("hello", TextType.BOLD)
        node2 = TextNode("hi", TextType.BOLD)
        self.assertNotEqual(node, node2, "TextNodes with different text should not be equal")

    def test_textnode_inequality_type(self):
        node = TextNode("hello", TextType.BOLD)
        node2 = TextNode("hello", TextType.ITALIC)
        self.assertNotEqual(node, node2, "TextNodes with different types should not be equal")

    def test_textnode_inequality_url(self):
        node = TextNode("link", TextType.LINK, "https://a.com")
        node2 = TextNode("link", TextType.LINK, "https://b.com")
        self.assertNotEqual(node, node2, "TextNodes with different URLs should not be equal")

    def test_textnode_url_default(self):
        node = TextNode("hello", TextType.CODE)
        node2 = TextNode("hello", TextType.CODE, None)
        self.assertEqual(node, node2, "Default URL None should result in equal TextNodes")

if __name__ == "__main__":
    unittest.main()