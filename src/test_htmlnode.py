import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_node_01(self):
        test_dict = {"href": "https://www.google.com","target": "_blank",}
        node_01 = HTMLNode(props=test_dict)
        node_01.props_to_html()

    def test_node_02(self):
        test_dict = {"href": "https://www.google.com",}
        node_02 = HTMLNode(props=test_dict)
        node_02.props_to_html()


if __name__ == "main":
    unittest.main()
