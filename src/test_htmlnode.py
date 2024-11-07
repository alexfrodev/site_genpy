import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_node_06(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        
        result = node.to_html()
        print(result)

    def test_parent_02(self):
        node = ParentNode(
    "ul",
    [
        LeafNode("li", "Item 1", props={"class": "first"}),
        LeafNode("li", "Item 2"),
        LeafNode("li", "Item 3", props={"id": "third-item"}),
    ]
)
# Expected Output: <ul><li class="first">Item 1</li><li>Item 2</li><li id="third-item">Item 3</li></ul>
        
        print(node.to_html())


    def test_parent_03(self):
        node = ParentNode(
    "div",
    [
        ParentNode(
            "section",
            [
                LeafNode("h1", "Title"),
                LeafNode("p", "This is a paragraph."),
            ]
        ),
        ParentNode(
            "footer",
            [
                LeafNode("p", "Footer content"),
            ]
        ),
    ]
)
        print(node.to_html())


    def  test_parent_04(self):
        node = ParentNode(
    "article",
    [
        ParentNode("header", [LeafNode("h1", "Article Title")]),
        ParentNode("section", [
            LeafNode("p", "First paragraph."),
            ParentNode("div", [LeafNode("p", "Nested paragraph in div.")]),
        ]),
        ParentNode("footer", [])
    ]
)
        print(node.to_html())

if __name__ == "main":
    unittest.main()
