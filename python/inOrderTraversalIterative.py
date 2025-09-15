class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        

# Time -> 0(N) Space -> 0(1)
def inOrderTraversalIterative(tree, callback):
    prevNode, currNode = None, tree
    while currNode is not None:
        if prevNode is None or prevNode == currNode.parent:
            if currNode.left is not None:
                nextNode = currNode.left
            else:
                callback(currNode)
                nextNode = currNode.right if currNode.right is not None else currNode.parent
        elif prevNode == currNode.left:
            callback(currNode)
            nextNode = currNode.right if currNode.right is not None else currNode.parent
        else:
            nextNode = currNode.parent
        
        prevNode = currNode
        currNode = nextNode
    
    
def callback(node):
    print(node.value)
    

root = BinaryTree(value=1)
root.left = BinaryTree(value=4, parent=root)
root.right = BinaryTree(value=2, parent=root)
inOrderTraversalIterative(root, callback)