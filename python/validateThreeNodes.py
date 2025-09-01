class BST:
    def __init__(self, value):
        self.value = value
        
        self.left = None
        self.right = None
        

# Time -> 0(h) Space -> 0(1)
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    curr = nodeOne
    found = False
    
    while curr != None:
        if curr == nodeThree:
            return False
        if curr == nodeTwo:
            found = True
            break
        if nodeTwo.value > curr.value:
            curr = curr.right
        else:
            curr = curr.left
    if found:
        curr = nodeTwo      
        while curr != None:
            if nodeThree == curr:
                return True
            if nodeThree.value > curr.value:
                curr = curr.right
            else:
                curr = curr.left
            
    while nodeThree != None:
        if nodeThree == nodeOne:
            return False
        if nodeTwo == nodeThree:
            found = True
            break
        if nodeTwo.value > nodeThree.value:
            nodeThree = nodeThree.right
        else:
            nodeThree = nodeThree.left
    if found:
        while nodeTwo != None:
            if nodeOne == nodeTwo:
                return True
            if nodeOne.value > nodeTwo.value:
                nodeTwo = nodeTwo.right
            else:
                nodeTwo = nodeTwo.left
        
    return False