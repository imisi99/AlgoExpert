def cycleInGraph(edges):
    table = {}
    
    for i in range(len(edges)):
        table[i] = 0
    
    for i in range(len(edges)):
        if table[i] == 2:
            continue
        if checkCycle(i, edges, table):
            return True
        
    return False


def checkCycle(node, edges, table):
    edge = edges[node]
    table[node] = 1
    
    for vertice in edge:
        if table[vertice] == 2:
            continue
        
        if table[vertice] == 1:
            return True
        
        if checkCycle(vertice, edges, table):
            return True
    
    table[node] = 2
    return False


print(cycleInGraph([[1, 3], [2, 3, 4], [0], [], [2, 5], []]))