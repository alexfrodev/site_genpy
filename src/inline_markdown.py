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




def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        extract_list = extract_markdown_images(node.text)

        if len(extract_list) == 0:
            new_nodes.append(node)
            continue

        original_text = node.text
        for image_alt, image_url in extract_list:

            before_link, original_text = original_text.split(f"![{image_alt}]({image_url})", 1)

            if before_link:
                new_nodes.append(TextNode(before_link, TextType.NORMAL))

            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        extract_list = extract_markdown_links(node.text)

        if len(extract_list) == 0:
            new_nodes.append(node)
            continue

        original_text = node.text
        for image_alt, image_link in extract_list:

            before_link, original_text = original_text.split(f"[{image_alt}]({image_link})", 1)

            if before_link:
                new_nodes.append(TextNode(before_link, TextType.NORMAL))

            new_nodes.append(TextNode(image_alt, TextType.LINK, image_link))

        if original_text:
            new_nodes.append(TextNode(original_text, TextType.NORMAL))

    return new_nodes


