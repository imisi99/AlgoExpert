class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        
        self.left = left
        self.right = right
        

class TreeInfo:
    def __init__(self, min, max, valid, sum=0, size=0, total=0):
        self.min = min
        self.max = max
        self.size = size
        self.sum = sum
        self.total = total
        self.valid = valid
        
        
# Time -> 0(N) Space -> 0(d) where d is the max height of the tree
def sumBsts(tree):
    return sumBst(tree).total
    
def sumBst(tree):
    if tree == None:
        return TreeInfo(min=float("inf"), max=float("-inf"), valid=True)

    leftTreeInfo = sumBst(tree.left)
    rightTreeInfo = sumBst(tree.right)
    
    
    valid = False
    if leftTreeInfo.valid and rightTreeInfo.valid:
        if tree.value > leftTreeInfo.max and tree.value <= rightTreeInfo.min:
            valid = True
            
    bstSum = 0
    size = 0
    minVal = min(tree.value, leftTreeInfo.min, rightTreeInfo.min)
    maxVal = max(tree.value, leftTreeInfo.max, rightTreeInfo.max)
    total = leftTreeInfo.total + rightTreeInfo.total
    
    if valid:
        bstSum = leftTreeInfo.sum + rightTreeInfo.sum + tree.value
        size = leftTreeInfo.size + rightTreeInfo.size + 1
        
        if size > 2:
            total = bstSum
    
    return TreeInfo(min=minVal, max=maxVal, valid=valid, sum=bstSum, size=size, total=total)

left = BinaryTree(1)
right = BinaryTree(3)
tree = BinaryTree(2, left=left, right=right)
print(sumBsts(tree))