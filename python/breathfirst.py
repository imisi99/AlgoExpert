class Node():
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
        

# Time -> 0(v+e), Space -> 0(v) 
def breathfirst(array, node):
    queue = []
    queue.append(node)
    
    while len(queue) > 0:
        node = queue[0]
        queue = queue[1:]
        array.append(node.value)
        if len(node.children) > 0:
            for val in node.children:
                queue.append(val)
    
    return array


children = [Node(
                value="B",
                children=[Node(value="E"), Node(value="F")]
            ),
            Node(
                value="C"
            ),
            Node(value="D")]

node = Node(
    value="A",
    children=children
)
print(breathfirst([], node))