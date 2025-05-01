from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("ParentNode must have a tag.")
        if children is None:
            raise ValueError("ParentNode must have children.")
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag.")
        if not self.children:
            raise ValueError("ParentNode must have children.")

        props = self.props_to_html()
        props_str = f"{props}" if props else ""
        inner_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{props_str}>{inner_html}</{self.tag}>"
            


# node = ParentNode(
#     "p",
#     [
#         LeafNode("b", "Bold text"),
#         LeafNode(None, "Normal text"),
#         LeafNode("i", "italic text"),
#         LeafNode(None, "Normal text"),
#     ],
# )

# print(node.to_html())