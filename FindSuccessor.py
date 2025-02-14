# This is an input class
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    if tree is None:
        return
    if tree.value == node.value:
        return
    if tree.left:
        findSuccessor(tree.left, node)
    if tree.right:
        findSuccessor(tree.right, node)
    return None
