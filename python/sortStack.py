# Time -> 0(N^2) Space -> 0(N)
def sortStack(stack):
    result = []
    lenStack = len(stack)
    
    while lenStack > 0:
        subStack = stack.copy()
        minVal = float("inf")
        while len(subStack) > 0:
            last = subStack.pop()
            if last < minVal:
                minVal = last
        result.append(minVal)
        stack = removeVal(stack, minVal)
        lenStack -= 1
        
    return result

def removeVal(stack, val):
    newStack, lenStack = [], len(stack)
    while lenStack > 0:
        last = stack.pop()
        if last == val:
            break
        newStack.append(last)
        lenStack -= 1
    
    newStack += stack
    return newStack


def sortStackInPlace(stack):
    sortStackRecursively(stack)
    return stack

def sortStackRecursively(stack):
    if len(stack) == 0:
        return
    
    top = stack.pop()
    sortStackRecursively(stack)
    insert(stack, top)
    
def insert(stack, val):
    if len(stack) == 0:
        stack.append(val)
        return
    top = stack[len(stack)-1]
    if val < top:
        stack.pop()
        insert(stack, val)
        stack.append(top)
        return
    else:
        stack.append(val)
        return
    
print(sortStack([4, 4, 2, 6, 7, 1]))
print(sortStackInPlace([4, 4, 2, 6, 7, 1]))