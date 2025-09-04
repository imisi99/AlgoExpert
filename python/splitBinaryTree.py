class BinaryTree:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None
        

def getSplit(tree):
    sum = getSum(tree)
    _, split = findSplit(tree, sum/2)
    if split:
        return sum / 2
    return 0
    


def findSplit(tree, sum):
    if tree == None:
        return 0, False
    leftTree, splitLeft = findSplit(tree.left, sum)
    rightTree, splitRight = findSplit(tree.right, sum)
    
    currTree = leftTree + rightTree + tree.value
    split = splitRight or splitLeft or currTree == sum
    return currTree, split


def getSum(tree):
    if tree == None:
        return 0
    return tree.value + getSum(tree.left) + getSum(tree.right)