from block_markdown import markdown_to_blocks, markdown_to_html_node
import os
from pathlib import Path



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    for source_path in Path(dir_path_content).iterdir():
        dest_path = Path(dest_dir_path) / source_path.stem
        if os.path.isfile(source_path):
            generate_page(source_path, template_path, f"{dest_path}.html")
        else:
            generate_pages_recursive(source_path, template_path, dest_path)




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
