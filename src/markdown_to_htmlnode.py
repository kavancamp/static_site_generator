from markdown_to_blocks import *
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from text_to_textnode import text_to_textnodes
from textnode import text_node_to_html_node



def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown) #Split the Markdown into chunks — paragraphs, headings, lists, etc.
    children = [] #Create an empty children list to collect the converted HTML block nodes.
    
    for block in blocks: 
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.CODE:
            lines = block.split("\n")
            code_text = "\n".join(line.strip() for line in lines[1:-1])  # strip first and last lines/leading spaces
            code_node = LeafNode("code", code_text)  # Wrap the content in <code> inside a <pre> block.
            block_node = ParentNode("pre", [code_node])

        elif block_type == BlockType.HEADING:
            level = len(block.split(" ")[0]) # count '#', h1 or h2 etc
            tag = f"h{level}"
            content = block[level + 1:].strip() #remove heading
            text_nodes = text_to_textnodes(content)
            inline_nodes = [text_node_to_html_node(node) for node in text_nodes]
            block_node = ParentNode(tag, inline_nodes) # wrapping content
            
        elif block_type == BlockType.QUOTE:
            quote_text = "\n".join([line[1:].strip() for line in block.splitlines() if line.startswith(">")])
            text_nodes = text_to_textnodes(quote_text)
            inline_nodes = [text_node_to_html_node(node) for node in text_nodes]
            block_node = ParentNode("blockquote", inline_nodes) #quote wrapper
            
        elif block_type == BlockType.UNORDERED_LIST:
            items = block.split("\n")
            li_nodes = []
            for item in items:
                item_text = item[2:].strip() 
                item_text_nodes = text_to_textnodes(item_text)
                li_nodes.append(ParentNode("li", [text_node_to_html_node(n) for n in item_text_nodes]))
            block_node = ParentNode("ul", li_nodes) # wrapped in <ul> items become <li>
        elif block_type == BlockType.ORDERED_LIST:
            items = block.split("\n")
            li_nodes = []
            for item in items:
                dot_index = item.find(".")
                item_text = item[dot_index + 1:].strip()
                item_text_nodes = text_to_textnodes(item_text)
                li_nodes.append(ParentNode("li", [text_node_to_html_node(n) for n in item_text_nodes]))
            block_node = ParentNode("ol", li_nodes) # wrapped in <ul> items become <li>
        else: #if nothing else, paragraph
            text_nodes = text_to_textnodes(block)
            inline_nodes = [text_node_to_html_node(node) for node in text_nodes]
            block_node = ParentNode("p", inline_nodes)
        children.append(block_node)
    return ParentNode("div", children)

