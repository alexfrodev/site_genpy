from types import new_class
from block_markdown import markdown_to_blocks, markdown_to_html_node
import os

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block[2:]
        else:
            raise Exception("No h1 header")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        md_source = file.read()

    with open (template_path, "r") as file:
        template = file.read()

    node = markdown_to_html_node(md_source)
    html_content = node.to_html()
    title = extract_title(md_source)

    replacements = {
            "{{ Title }}": title,
            "{{ Content }}": html_content,
    }
    for old, new in replacements.items():
        template = template.replace(old, new)
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(template)

    print("Page Generated!")
