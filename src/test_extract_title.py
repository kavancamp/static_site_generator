import unittest
from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_no_space_in_title(self):
        md = """
This is a paragraph.

#This is a heading

## This is another heading
"""
        node = extract_title(md)
        expected = "This is a heading"
        self.assertEqual(node, expected)
        

    def test_space_in_title(self):
        md = """
This is a paragraph.

# This is a heading

## This is another heading
"""
        node = extract_title(md)
        expected = "This is a heading"
        self.assertEqual(node, expected)

    def test_raises_when_no_h1(self):
        md = """
        This is just a paragraph.
        ## This is a level 2 heading.
        """
        with self.assertRaises(Exception) as context:
            extract_title(md)
        
        # Optional: check the message
        self.assertEqual(str(context.exception), "No h1 header present")
        
if __name__ == "__main__":
    unittest.main()
    