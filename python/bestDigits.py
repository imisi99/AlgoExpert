# Time -> 0(N) Space -> 0(N)
def bestDigits(numbers, numDigits):
    stack = []
    for digit in numbers:
        if numDigits > 0:
            i = len(stack) - 1
            while i >= 0:
                if numDigits > 0:
                    if int(digit) > int(stack[i]):
                        stack.pop()
                        numDigits -= 1
                        i -= 1
                    else:
                        break
                else:
                    break
        
        stack.append(digit)
     
    result = "".join(stack)
    if numDigits > 0 :
        return result[:len(result)-numDigits]
    
    return result


print(bestDigits("23333", 2))