class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    
    def InOrder(self, array):
        if self.left != None:
            self.left.InOrder(array)
        array.append(self.value)
        if self.right != None:
            self.right.InOrder(array)
            
        return array
    
    
    def PreOrder(self, array):
        array.append(self.value)
        if self.left != None:
            self.left.PreOrder(array)
        if self.right != None:
            self.right.PreOrder(array)
            
        return array
    
    
    def PostOrder(self, array):
        if self.left != None:
            self.left.PostOrder(array)
        if self.right != None:
            self.right.PostOrder(array)
        array.append(self.value)
        
        return array
        
