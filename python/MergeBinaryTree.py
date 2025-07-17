class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
 
        
# Time -> 0(N)  Space -> 0(h) where N is the number of node in the first tree and h is the max height 
def MergeBinaryTree(tree1, tree2: BinaryTree) -> BinaryTree:
    left_stack, right_stack = [], []
    left_stack.append(tree1)
    right_stack.append(tree2)
    
    while len(left_stack) > 0:
        left = left_stack.pop()
        right = right_stack.pop()
        
        
        left.value += right.value
        
        if left.left == None:
            left.left = right.left
        elif left.left != None and right.left != None:
            left_stack.append(left.left)
            right_stack.append(right.left)
            
        if left.right == None:
            left.right = right.right
        elif left.right != None and right.right != None:
            left_stack.append(left.right)
            right_stack.append(right.right)
            
        
    return tree1

