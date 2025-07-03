class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    
    def populate(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        left = self
        for val in array[:len(array)//2]:
            left.left = BinaryTree(val)
            left = left.left
        right = self
        for val in array[len(array)//2:]:
            right.right = BinaryTree(val)
            right = right.right
        print(array[:len(array)//2])
        print(array[len(array)//2:])
        

# Time -> 0(N) Space -> 0(h)-worst case 0(N) where h is the max height of the tree
def BalancedBinaryTree(tree):
    if tree == None:
        return 0, 0, True
    
    left_tree = BalancedBinaryTree(tree.left)
    right_tree = BalancedBinaryTree(tree.right)

    left_height = max(left_tree[0], left_tree[1]) + 1
    right_height = max(right_tree[0], right_tree[1]) + 1
    is_balanced = left_tree[2] and right_tree[2] and abs(left_height - right_height) <= 1
    
    print(left_height, right_height, is_balanced)
    return left_height, right_height, is_balanced
        
tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.left.right = BinaryTree(3)   

print(BalancedBinaryTree(tree))
