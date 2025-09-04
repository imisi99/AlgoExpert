# Time -> 0(N) Space -> 0(N)
def reversePolishNotation(array: list):
    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y :x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: int(x / y)
    }

    stack = []
    
    for char in array:
        if char in ops:
            secondVal = stack.pop()
            firstVal = stack.pop()
            result = ops[char](firstVal, secondVal)
            stack.append(result)
        else:
            stack.append(int(char))
    return stack[0]

print(reversePolishNotation(["3", "4", "7", "*", "+"]))