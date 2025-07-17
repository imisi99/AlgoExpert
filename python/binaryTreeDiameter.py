class BinaryTree:
    def __init__(self, value):
        self.value = value
        
        self.left = None
        self.right = None
        
    
    def GetDiameter(self):
        if self == None:
            return TreeInfo(0, 0)
        
        leftTreeInfo = self.left.GetDiameter()
        rightTreeInfo = self.right.GetDiameter()
        
        maxdiameter = max(leftTreeInfo.diameter, rightTreeInfo.diameter, (rightTreeInfo.height + leftTreeInfo.height))
        height = max(leftTreeInfo.height, rightTreeInfo.height) + 1
        
        return TreeInfo(maxdiameter, height)
    
        
class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height
        
        
def getMaxDiameter(tree):
    return tree.GetDiameter().diameter