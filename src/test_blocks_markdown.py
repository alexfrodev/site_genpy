import unittest

from block_markdown import (
        markdown_to_blocks,
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


if __name__ == "__main__":
    unittest.main()

