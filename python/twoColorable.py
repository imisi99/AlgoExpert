# Time -> 0(v + e) Space -> 0(e) where v is the vertices(length of the edge) and e is the max lenght of a edge 
def twoColorable(edges: list):
    table = {}
    edge = 0

    while edge < len(edges):
        if edge not in table:
            table[edge] = "blue"
        color = table[edge]
        
        for node in edges[edge]:
            if node not in table:
                table[node] = setColor(color)
            
            color1 = table[node]
            
            if color == color1:
                return False
            
        edge += 1
        
    return True

                
def setColor(color):
    if color == "blue":
        return "yellow"
    return "blue"


print(twoColorable([[1], [0]]))
print(twoColorable([[1, 2], [0, 2], [0, 1]]))