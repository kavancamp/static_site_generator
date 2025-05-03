import unittest
from markdown_to_htmlnode import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_heading(self):
        md = "# Welcome"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><h1>Welcome</h1></div>")
        
    def test_paragraph(self):
        markdown = "This is a paragraph."
        html_node = markdown_to_html_node(markdown)
        p_node = html_node.children[0]
        self.assertEqual(p_node.tag, "p")
        self.assertEqual(p_node.to_html(), "<p>This is a paragraph.</p>")
        
    def test_codeblock(self):
        md = "```\nThis is text that _should_ remain\nthe **same** even with inline stuff\n```"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>"
        )
        
    def test_unordered_list(self):
        markdown = "- Item 1\n- Item 2"
        html_node = markdown_to_html_node(markdown)

        ul_node = html_node.children[0]
        self.assertEqual(ul_node.tag, "ul")
        self.assertEqual(ul_node.to_html(), "<ul><li>Item 1</li><li>Item 2</li></ul>")
        
    def test_ordered_list(self):
        markdown = "1. First\n2. Second"
        html_node = markdown_to_html_node(markdown)
        ol_node = html_node.children[0]
        self.assertEqual(ol_node.tag, "ol")
        self.assertEqual(ol_node.to_html(), "<ol><li>First</li><li>Second</li></ol>")
        
    def test_quote(self):
        markdown = "> quoted text"
        html_node = markdown_to_html_node(markdown)
        quote_node = html_node.children[0]
        self.assertEqual(quote_node.tag, "blockquote")
        self.assertEqual(quote_node.to_html(), "<blockquote>quoted text</blockquote>")
    
    
if __name__ == "__main__":
    unittest.main()