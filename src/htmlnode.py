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