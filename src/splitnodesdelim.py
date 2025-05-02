from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # If it's not plain text, leave it untouched
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise Exception(f"Unmatched delimiter `{delimiter}` in text: {node.text}")

        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                # Even index -> plain text
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Odd index -> delimited text
                new_nodes.append(TextNode(part, text_type))

    return new_nodes
