import unittest
from htmlnode import HTMLNode  

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_single_attr(self):
        node = HTMLNode("a", "Link", props={"href": "https://example.com"})
        expected = 'href="https://example.com"'
        actual = node.props_to_html()
        self.assertEqual(
            actual, expected,
            f"\nFailed Single Attribute Test:\nExpected: {repr(expected)}\nGot:      {repr(actual)}"
        )

    def test_props_to_html_multiple_attrs(self):
        node = HTMLNode("a", "Click", props={"target": "_blank", "href": "https://google.com"})
        expected = 'href="https://google.com" target="_blank"'  # assuming sorted keys
        actual = node.props_to_html()
        self.assertEqual(
            actual, expected,
            f"\nFailed Multiple Attributes Test:\nExpected: {repr(expected)}\nGot:      {repr(actual)}"
        )

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "Text", props={})
        expected = ''
        actual = node.props_to_html()
        self.assertEqual(
            actual, expected,
            f"\nFailed Empty Props Test:\nExpected: {repr(expected)}\nGot:      {repr(actual)}"
        )
    
if __name__ == "__main__":
    unittest.main()
    

