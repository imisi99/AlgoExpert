class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def inOrderTraversal(self, array):
        if self.left != None: 
            self.left.inOrderTraversal(array)
        array.append(self.value)
        if self.right != None:
            self.right.inOrderTraversal(array)
        return array
    
    def ReverseInOrderTraversal(self, array):
        if self.right != None:
            self.right.ReverseInOrderTraversal(array)
        array.append(self.value)
        if self.left != None:
            self.left.ReverseInOrderTraversal(array)
        return array
    
    
def populateBST(bst, start, end, array):
    if end < start:
        return
    mid = (end + start) // 2
    bst = BST(array[mid])
    bst.left = populateBST(bst, start, mid-1, array)
    bst.right = populateBST(bst, mid+1, end, array)
    
    return bst



# Time -> 0(N) Space -> 0(N)   n = number of nodes in BST
def findKthLargestValue(bst, k):
    array = bst.inOrderTraversal([])
    return array[len(array)-k]
    
    
# Time -> 0(h + k) Space -> 0(h)  h = max height of tree 
def findKthLargestValue2(bst, k, visited):
    if bst == None:
        return None
    right = findKthLargestValue2(bst.right, k, visited)
    if right != None:
        return right
    visited[0] += 1
    if visited[0] == k:
        return bst.value
    return findKthLargestValue2(bst.left, k, visited)

           
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 19, 39, 40, 43]
bst = populateBST(None, 0, len(array)-1, array)
print(bst.inOrderTraversal([]))
print(bst.ReverseInOrderTraversal([]))
print(findKthLargestValue(bst, 12))
print(findKthLargestValue2(bst, 12, [0]))

