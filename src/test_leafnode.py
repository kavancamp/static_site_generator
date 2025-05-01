import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_plain_text(self):
        node = LeafNode(None, "Just plain text")
        expected = "Just plain text"
        self.assertEqual(node.to_html(), expected, f"Expected: '{expected}', Got: '{node.to_html()}'")

    def test_paragraph_node(self):
        node = LeafNode("p", "This is a paragraph.")
        expected = "<p>This is a paragraph.</p>"
        self.assertEqual(node.to_html(), expected, f"Expected: '{expected}', Got: '{node.to_html()}'")

    def test_anchor_node_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
        expected = '<a href="https://www.google.com" target="_blank">Click me!</a>'
        self.assertEqual(node.to_html(), expected, f"Expected: '{expected}', Got: '{node.to_html()}'")

    def test_missing_value_raises_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)
            
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    

if __name__ == '__main__':
    unittest.main()
