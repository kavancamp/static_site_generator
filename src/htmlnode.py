class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props if props is not None else {}


    def to_html(self):
        raise NotImplementedError("This function is not yet implemented.")
    
    def props_to_html(self):
        if not self.props:
            return ""
        return " ".join(f'{key}="{value}"' for key, value in sorted(self.props.items()))
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

    #node = HTMLNode(
    #tag="a",
    #props={
     #   "href": "https://www.google.com",
     #   "target": "_blank"
    #}
#)

#print(node.props_to_html())
#print(node.__repr__())
class LeafNode(HTMLNode):
    def __init__(self, tag, value,  props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag=tag, value=value, children=None, props=props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value
        else:
            props = self.props_to_html()
            space = " " if props else ""
            return f"<{self.tag}{space}{props}>{self.value}</{self.tag}>"
    
#node1 = LeafNode("p", "This is a paragraph.")
#print(node1.to_html())
#node2 = LeafNode("a", "Click here", {"href": "https://www.example.com", "target": "_blank"})
#print(node2.to_html())
#node3 = LeafNode(None, "Just some raw text")
#print(node3.to_html())

class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props=None):
        if tag is None or children is None:
            raise ValueError("Parent Node must have a tag, and children.")
        super().__init__(tag=tag, children=children, props=props)
    def to_html(self):
            if self.value is None:
                raise ValueError("LeafNode must have a value.")
            if self.tag is None:
                return self.value
            else:
                props = self.props_to_html()
                space = " " if props else ""
                return f"<{self.tag}{space}{props}>{self.value}</{self.tag}>"
