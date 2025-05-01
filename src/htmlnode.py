class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError("This function is not yet implemented.")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    

    #node = HTMLNode(
    #tag="a",
    #props={
     #   "href": "https://www.google.com",
     #   "target": "_blank"
    #}
#)

#print(node.props_to_html())
#print(node.__repr__())




