# Time -> 0(N)      Space -> 0(N)
def nextGreaterElement(array):
    stack = []
    result = [-1] * len(array)
    i = 0
    while i < len(array)*2:
        idx = i % len(array)
        while len(stack) > 0 and array[idx] > array[stack[-1]]:
            result[stack.pop()] = array[idx]
        stack.append(idx)
        i += 1
        
    return result

print(nextGreaterElement([2, 5, -3, -4, 6, 7, 2]))
            