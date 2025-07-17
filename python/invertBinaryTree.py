class BinaryTree:
    def __init__(self, value):
        self.value = value
        
        self.left = None
        self.right = None
        
    
    def Inorder(self, array):
        if self.left != None:
            self.left.Inorder(array)
        array.append(self.value)
        if self.right != None:
            self.right.Inorder(array)
            
        return array
    
    # Time -> 0(N) Space -> 0(h) where h is the max height of the tree
    def invertTree(self):

        self.left, self.right = self.right, self.left
        if self.left != None:
            self.left.invertTree()
        if self.right != None:
            self.right.invertTree()
        
    
tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.left.left = BinaryTree(4)
tree.left.right = BinaryTree(5)
tree.right = BinaryTree(3)
tree.right.left = BinaryTree(6)
tree.right.right = BinaryTree(7)


array = tree.Inorder([])
tree.invertTree()
invertarray = tree.Inorder([])

print(array == invertarray[::-1])

