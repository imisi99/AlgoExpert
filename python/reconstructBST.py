class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    
    def Insert(self, value):
        while self != None:
            if value < self.value:
                if self.left == None:
                    self.left = BST(value)
                    break
                else:
                    self = self.left
            else:
                if self.right == None:
                    self.right = BST(value)
                    break
                else:
                    self = self.right
                    
    
    def PreOrder(self, array):
        array.append(self.value)
        if self.left != None:
            self.left.PreOrder(array)
        if self.right != None:
            self.right.PreOrder(array)
        return array
    
    
    
preOrderTraversal = [10, 4, 2, 1, 5, 17, 19, 18]


# Time -> 0(NlogN) Space -> 0(h)
def buildFromPreOrder(array):
    bst = BST(array[0])
    for val in array[1:]:
        bst.Insert(val)
        
    return bst


# Time -> 0(N) Space -> 0(h)    h is the height of the tree 
def buildFromPreOrder2(array):
    return RecursiveAddition(float("-inf"), float("inf"), array, [0])
    

def RecursiveAddition(lowerBound, upperBound, array, rootidx):
    if rootidx[0] == len(array):
        return None
    
    rootvalue = array[rootidx[0]]
    if rootvalue < lowerBound or rootvalue >= upperBound:
        return None
    
    rootidx[0] += 1
    leftsubtree = RecursiveAddition(lowerBound, rootvalue, array, rootidx)
    rightsubtree = RecursiveAddition(rootvalue, upperBound, array, rootidx)
    
    return BST(rootvalue, leftsubtree, rightsubtree)
        

bst = buildFromPreOrder(preOrderTraversal)
bst2 = buildFromPreOrder2(preOrderTraversal)
print(bst2.PreOrder([]) == preOrderTraversal)
print(bst.PreOrder([]) == preOrderTraversal)
