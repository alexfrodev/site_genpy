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
        prop = super().props_to_html()
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{prop}>{self.value}</{self.tag}>"
