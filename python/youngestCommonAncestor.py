class AncestryTree():
    def __init__(self, value, ancestor=None):
        self.value = value
        self.ancestor = ancestor
    

# Time -> 0(log(N)) Space -> 0(log(N))
def getYoungestCommonAncestor(top: AncestryTree, node1: AncestryTree, node2: AncestryTree) -> AncestryTree:
    ancestor_list = {}
    while node1 is not None:
        ancestor_list[node1] = True
        node1 = node1.ancestor
    while node2 is not None:
        if node2 in ancestor_list:
            return node2
        node2 = node2.ancestor
    return top


# Time -> 0(log(N)) Space -> 0(1)
def getYoungestCommonAncestor1(top: AncestryTree, node1: AncestryTree, node2: AncestryTree) -> AncestryTree:
    node1_count = node1
    node2_count = node2
    node1_c, node2_c = 0, 0
    while node1_count != None:
        node1_c += 1
        node1_count = node1_count.ancestor
    while node2_count != None:
        node2_c += 1
        node2_count = node2_count.ancestor
    
    if node1_c > node2_c:
        return level(node1, node2, node1_c-node2_c)
    else:
        return level(node2, node1, node2_c-node1_c)
    
    
def level(high: AncestryTree, level: AncestryTree, diff: int) -> AncestryTree:
    while diff > 0:
        diff -= 1
        high = high.ancestor
    
    while high != level:
        high = high.ancestor
        level = level.ancestor
    return level

top = AncestryTree(value=1)
a = AncestryTree(value=2, ancestor=top)
b = AncestryTree(value=3, ancestor=top)
node1 = AncestryTree(value=4, ancestor=a)
node2 = AncestryTree(value=7, ancestor=top)
print(getYoungestCommonAncestor1(top, node1, node2).value)