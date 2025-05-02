import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )


    def test_values(self):
        node = HTMLNode(
            "div", 
            "I wish I could read"
            )
        self.assertEqual(
            node.tag, "div", 
            #f"Expected: 'div', Got: {node.tag}")
        )

    def test_repr(self):
        node = HTMLNode("p", "What a strange world", None, {"class": "primary"})
        expected = "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})"
        actual = node.__repr__()
        self.assertEqual(
            actual,
            expected,
            #f"Expected: {expected}, Got: {actual}"
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        expected = "<p>Hello, world!</p>"
        actual = node.to_html()
        self.assertEqual(
            actual,
            expected,
            #f"Expected: {expected}, Got: {actual}
        )

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

if __name__ == "__main__":
    unittest.main()