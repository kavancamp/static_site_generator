import unittest
from extract_markdown import *

class TestExtractMarkdownImages(unittest.TestCase):
    
    def test_single_image(self):
        text = "check this image: ![Alt text](https://example.com/img.png)"
        expected = [("Alt text", "https://example.com/img.png")]
        self.assertEqual(extract_markdown_images(text), expected)
        #print(f"test_single_image \n expected: {expected}, \n got: {extract_markdown_images(text)} ")
        
    def test_multiple_images(self):
        text = "First: ![Cat](https://img.com/cat.jpg), Second: ![Dog](https://img.com/dog.jpg)"
        expected = [
            ("Cat", "https://img.com/cat.jpg"),
            ("Dog", "https://img.com/dog.jpg")
        ] 
        self.assertEqual(extract_markdown_images(text), expected)
        #print(f"test_multiple_images \n expected: {expected}, \n got: {extract_markdown_images(text)} ")
    
    def test_special_characters_in_alt(self):
        text = "![A cat & a dog](https://example.com/catdog.png)"
        expected = [("A cat & a dog", "https://example.com/catdog.png")]
        self.assertEqual(extract_markdown_images(text), expected)
        #print(f"test_special_characters_in_alt \n expected: {expected}, \n got: {extract_markdown_images(text)} ")
    
    def test_no_images(self):
        text = "This has no images, just text and maybe [a link](https://example.com)."
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)   
        #print(f"test_no_images \n expected: {expected}, \n got: {extract_markdown_images(text)} ")
    
    def test_encoded_spaces_in_url(self):
        text = "![Alt](https://example.com/my%20image.png)"
        expected = [("Alt", "https://example.com/my%20image.png")]
        self.assertEqual(extract_markdown_images(text), expected)
        #print(f"test_encoded_spaces \n expected: {expected}, \n got: {extract_markdown_images(text)} ")
        
    def test_malformed_image_syntax(self):
        text = "![Missing URL] or [not an image](http://bad.com)"
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)
        #print(f"test_encoded_spaces \n expected: {expected}, \n got: {extract_markdown_images(text)} ")

    def test_images_and_links(self):
        text = "![Image1](http://img1.com) and [Link](http://example.com) and ![Image2](http://img2.com)"
        expected = [("Image1", "http://img1.com"), ("Image2", "http://img2.com")]
        self.assertEqual(extract_markdown_images(text), expected)
        #print(f"test_encoded_spaces \n expected: {expected}, \n got: {extract_markdown_images(text)} ")    
    
    
class TestExtractMarkdownLinks(unittest.TestCase):
    def test_single_link(self):
        text = "This is a [link](http://example.com)"
        expected = [("link", "http://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)
        #print(f"test_single_link:\n expected: {expected}, \n got: {extract_markdown_links(text)} ") 

    def test_multiple_links(self):
        text = "Check [this](http://a.com) and [that](https://b.org)"
        expected = [("this", "http://a.com"), ("that", "https://b.org")]
        self.assertEqual(extract_markdown_links(text), expected)
        #print(f"test_multiple_link:\n expected: {expected}, \n got: {extract_markdown_links(text)} ") 
        
    def test_no_links(self):
        text = "No links here, just text."
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)
        #print(f"test_no_link:\n expected: {expected}, \n got: {extract_markdown_links(text)} ") 
        
    def test_links_with_special_characters(self):
        text = "[foo bar](https://example.com/path?query=1&sort=asc)"
        expected = [("foo bar", "https://example.com/path?query=1&sort=asc")]
        self.assertEqual(extract_markdown_links(text), expected)
        #print(f"links_with_spec_char:\n expected: {expected}, \n got: {extract_markdown_links(text)} ") 
        
        
class TestSplitNodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes
        )

    def test_split_links(self):
        node = TextNode(
            "This is a [link](https://example.com) in a sentence with [another](https://second.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" in a sentence with ", TextType.TEXT),
                TextNode("another", TextType.LINK, "https://second.com"),
            ],
            new_nodes,
        )
        
    def test_no_links(self):
        node = TextNode("Just plain text here.", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(result, [node])
        #print(f"no links: {result}, {[node]}")

    def test_no_images(self):
        node = TextNode("No images in this text either.", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(result, [node])
        #print(f"no images: {result}, {[node]}")
        
if __name__ == "__main__":
    unittest.main()
