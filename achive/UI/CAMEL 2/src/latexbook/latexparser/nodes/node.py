from collections import namedtuple


class LeafNode(object):
    """An abstract class which represents a leaf node on a tree."""

    checkable = False  # Should we check against this node in the parser?
    allowed_children = False  # A leaf node can not have children.

    CheckLatexReturn = namedtuple("PreambleCapture", """
        inner_start_index, inner_end_index,
        outer_start_index, outer_end_index,
        arguments
    """)

    def __init__(self):
        """Initialise the leaf node."""
        self.position = 0  # The position of the node in the parent.

    def __str__(self):
        """Return a nicely printable string of the node."""
        return self.__class__.__name__

    def __repr__(self):
        """Return the canonical string representation of the node."""
        return "%s()" % (self.__class__.__name__)

    @classmethod
    def get_id(cls):
        """Return the ID of the current node."""
        return cls.__name__.lower()

    @classmethod
    def check_latex(cls, latex, nodes):
        """
        Check the given LaTeX text to see if it begins with the node's LaTeX command.

        Returns a list of all the matches.
        These matches should be instances of the 'CheckLatexReturn' namedtuple.
        """
        return []


class Node(LeafNode):
    """Extends upon LeafNode, by implementing children, creating potential for representation non-leaf nodes."""

    checkable = True  # Should we check against this node in the parser?
    allowed_children = True  # A regular node 'could' have children.

    def __init__(self, children=None):
        """Initialise the node."""
        super(Node, self).__init__()
        self.children = children
        # inner_start_index, inner_end_index, outer_start_index, outer_end_index, arguments

    def __repr__(self):
        """Return the canonical string representation of the node."""
        arguments = ""
        if isinstance(self.children, list):
            arguments += "children=["
            for child in self.children:
                if child != self.children[0]:
                    arguments += ", "
                arguments += repr(child)
            arguments += "]"
        return "%s(%s)" % (self.__class__.__name__, arguments)

    @classmethod
    def validate_arguments(cls, arguments):
        """Return if the given arguments are valid."""
        arguments = arguments.strip()
        return arguments != ""

    def add_children(self, children):
        """Add a list of children to the node."""
        if not isinstance(self.children, list):
            self.children = []

        next_position = len(self.children)
        for child in children:
            child.position = next_position
            next_position += 1
        self.children.extend(children)

    def add_child(self, child):
        """Add a single child to the node."""
        self.add_children([child])


# Not the most ideal way of implementing Node arguments,
# but it will allow for our arguments to have children nodes.
# Doing arguments this way allows us to do things such as making
# the level block's title contain other nodes such as A TextStyle.
class ArgumentNode(Node):
    """A node which represents an argument for the parent node."""

    def __init__(self, children=None):
        """Initialise the argument node."""
        super(ArgumentNode, self).__init__(children=children)


class TextNode(LeafNode):
    """A leaf node which just holds some plain text."""

    the_type = "text"

    def __init__(self, content):
        """Initialise the text leaf node."""
        super(TextNode, self).__init__()
        self.set_content(content)

    def __str__(self):
        """Return a nicely printable string of the node."""
        return self.content

    def __repr__(self):
        """Return the canonical string representation of the node."""
        return "%s(\"%s\")" % (self.__class__.__name__, self.content)

    @classmethod
    def validate_content(cls, content):
        """Return a boolean indicating if the content is acceptable for the Text node."""
        return content == " " if content.isspace() else content != ""

    def set_content(self, content):
        """Set the text, allowing us to change it if needed."""
        self.content = content.strip()
