import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_node_01(self):
        test_dict = {"href": "https://www.google.com","target": "_blank",}
        node_01 = HTMLNode(props=test_dict)
        result = node_01.props_to_html()
        print(result)

    def test_node_02(self):
        test_dict = {"href": "https://www.google.com",}
        node_02 = HTMLNode(props=test_dict)
        result = node_02.props_to_html()
        print(result)

    def test_node_03(self):
        node_03 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = node_03.to_html()
        print(result)

    def test_node_04(self):
        node_03 = LeafNode("p", "This is a paragraph of text.")
        result = node_03.to_html()
        print(result)

    def test_node_05(self):
        node_03 = LeafNode(tag=None, value="This is a paragraph of text.")
        result = node_03.to_html()
        print(result)


if __name__ == "main":
    unittest.main()
