from textnode import TextType, TextNode
import re



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        
        segments = node.text.split(delimiter)

        if len(segments) % 2 == 0:
            raise ValueError("Invalid markdown syntax, section not closed")

        for i, segment in enumerate(segments):
            if segment:
                if i % 2 == 0:
                    new_nodes.append(TextNode(segment, TextType.NORMAL))
                else:
                    new_nodes.append(TextNode(segment, text_type))
        
    
    return new_nodes



def extract_markdown_images(text):
    matches = re.findall(r"\[(.*?)\]+\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]+\((.*?)\)", text)
    return matches
