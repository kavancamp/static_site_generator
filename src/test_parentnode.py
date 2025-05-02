import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_basic(self):
        node = ParentNode(
            "div",
            [
                LeafNode(None, "Hello"),
                LeafNode("strong", "World"),
                LeafNode(None, "!")
            ]
        )
        expected = "<div>Hello<strong>World</strong>!</div>"
        actual = node.to_html()
        self.assertEqual(actual, expected, f"Expected: {expected}, Got: {actual}")

    def test_to_html_with_props(self):
        node = ParentNode(
            "section",
            [LeafNode(None, "Content")],
            props={"class": "main", "id": "top"}
        )
        expected = '<section class="main" id="top">Content</section>'
        actual = node.to_html()
        self.assertEqual(actual, expected, f"Expected: {expected}, Got: {actual}")

    def test_missing_tag_raises(self):
        with self.assertRaises(ValueError) as cm:
            ParentNode(None, [LeafNode(None, "oops")])
        self.assertEqual(str(cm.exception), "ParentNode must have a tag.")

    def test_missing_children_raises(self):
        with self.assertRaises(ValueError) as cm:
            ParentNode("div", None)
        self.assertEqual(str(cm.exception), "ParentNode must have children.")

    def test_empty_children_list_raises(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), "ParentNode must have children.")

if __name__ == "__main__":
    unittest.main()
