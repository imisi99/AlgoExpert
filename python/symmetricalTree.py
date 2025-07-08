class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
    def PreOrder(self, array: list) -> list:
        array.append(self.value)
        
        if self.left != None:
            array = self.left.PreOrder(array)
        if self.right != None:
            array = self.right.PreOrder(array)
        
        return array
    
    
    def InversePreOrder(self, array: list) -> list:
        array.append(self.value)
        if self.right != None:
            array = self.right.InversePreOrder(array)
        if self.left != None:
            array = self.left.InversePreOrder(array)
        
        return array
    
    
    
def PopulateBT() -> BinaryTree:
    tree = BinaryTree(1)
    tree.left = BinaryTree(2)
    tree.right = BinaryTree(2)
    
    left = tree.left
    right = tree.right
    
    left.left = BinaryTree(3)
    left.right = BinaryTree(4)
    
    right.left = BinaryTree(4)
    right.right = BinaryTree(3)
    
    return tree
    

# Time -> 0(N) Space -> 0(N)    
def Sol1() -> bool:
    arr1, arr2 = [], []
    
    tree = PopulateBT()
    if tree.left != None:
        arr1 = tree.left.PreOrder([])
    if tree.right != None:
        arr2 = tree.right.InversePreOrder([])
        
    return arr1 == arr2
    

# Time -> 0(N) Space -> 0(h) where h is the max height of the binary tree
def Sol2() -> bool:
    left_stack, right_stack = [], []
    
    tree = PopulateBT()
    left_stack.append(tree.left)
    right_stack.append(tree.right)
    
    while left_stack and right_stack:
        left_tree = left_stack.pop()
        right_tree = right_stack.pop()
        if left_tree == None and right_tree == None:
            continue
        
        if left_tree is None or right_tree is None or left_tree.value != right_tree.value:
            return False
        left_stack.append(left_tree.left)
        left_stack.append(left_tree.right)
        right_stack.append(right_tree.right)
        right_stack.append(right_tree.left)
            
            
    if left_stack or right_stack:
        return False
    
    return True    
        
        
    

print(Sol1())
print(Sol2())