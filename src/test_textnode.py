import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_02(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_eq_03(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertEqual(node, node2)

    def test_eq_04(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_to_html_normal(self):
        node = TextNode("Plain text", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, "Plain text")

    def test_to_html_img(self):
        node = TextNode("Image test", TextType.IMAGE, "www.test.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.props, {"src": "www.test.com", "alt": "Image test"},)





if __name__ == "__main__":
    unittest.main()
