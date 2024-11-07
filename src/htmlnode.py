class HTMLNode:
    def __init__(self, tag=None, value=None,
                 children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if isinstance(self.props, dict):
            result = "".join(f' {key}="{value}"' for key, value in self.props.items())
            return result
        return ""


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        else:
            prop = super().props_to_html()
            return f"<{self.tag}{prop}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("no tag provided")
        if self.children == None:
            raise ValueError("no children provided")

        prop = super().props_to_html()

        def recursive_html(children):
            if not children:
                return ""
            return children[0].to_html() + recursive_html(children[1:])

        children_html = recursive_html(self.children)
        return f"<{self.tag}{prop}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag},children: {self.children}, {self.props})"
