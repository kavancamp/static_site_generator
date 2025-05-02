from enum import Enum
import re

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    clean_blocks = [block.strip() for block in blocks if block.strip() != ""]
    return clean_blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"
    

def block_to_block_type(block):
    lines = block.splitlines()

    if len(lines) >= 2 and lines[0].strip().startswith("```") and lines[-1].strip().endswith("```"):
        return BlockType.CODE

    if re.match(r"^#{1,6} ", lines[0]):
        return BlockType.HEADING

    if all(line.strip().startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.strip().startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    if all(re.match(rf"^{i+1}\. ", line.strip()) for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


