import unittest

from generate_page import extract_title



class TestExtractTitle(unittest.TestCase):

    def test_extract(self):

        md = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

    * This is the first list item in a list block
    * This is a list item
    * This is another list item"""

        title = extract_title(md)

        self.assertEqual(
                "This is a heading", title,
        )

