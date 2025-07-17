class BinaryTree:
    def __init__(self, value):
        self.value = value
        
        self.left = None
        self.right = None
        
        
    def InOrder(self, array, node, idx) -> list:
        if self.left != None:
            self.left.InOrder(array, node, idx)
        array.append(self)
        idx.idx += 1
        if self.value == node.value:
            idx.store = idx.idx
        if self.right != None:
            self.right.InOrder(array, node, idx)
        
        return array
    
    
    
class Idx:
    def __init__(self):
        self.idx = 0
        self.store = -1


# Time -> 0(N) Space -> 0(N)
def getSuccessor(tree, node):
    idx = Idx()
    array = tree.InOrder([], node, idx)
    if idx.store >= len(array) or idx.store == -1:
        return None
    return array[idx.store]


tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.left.left = BinaryTree(3)
tree.left.right = BinaryTree(4)
tree.right = BinaryTree(5)

node = BinaryTree(12)


print(getSuccessor(tree, node).value if getSuccessor(tree, node) != None else None)