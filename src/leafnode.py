from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value,  props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value
        
        props = self.props_to_html()
        props_str = f"{props}" if props else ""
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
    
# node1 = LeafNode("p", "This is a paragraph.")
# print("expected: <p>This is a paragraph.</p>")
# print(f"received: {node1.to_html()}")
# node3 = LeafNode(None, "Just some raw text")
# print(node3.to_html())
# node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
# expected = "<a href=\"https://www.google.com\">Click me!</a>"
# print(node.to_html())
# print(expected)