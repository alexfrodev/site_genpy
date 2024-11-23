import unittest

from block_markdown import (
        markdown_to_blocks,
    block_to_block_type,
)



class TestSplitblocks(unittest.TestCase):
    def test_split_block(self):
        md = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

    * This is the first list item in a list block
    * This is a list item
    * This is another list item"""

        blocks = markdown_to_blocks(md)

        self.assertListEqual(
                [
    "# This is a heading",
    "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
    """* This is the first list item in a list block
    * This is a list item
    * This is another list item""",
                ],
                blocks,
        )


    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )



class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        block = "### This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(
                block_type,
                "heading",
        )
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), "heading")
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), "code")
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), "quote")
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), "unordered_list")
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), "ordered_list")
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), "paragraph")



if __name__ == "__main__":
    unittest.main()

