# Time: 0(N^2) Space: 0(N)
def threeNumberSum(array, targetSum):
    result = []
    table = {}
    result_ = {}
    for val in array:
        table[val] = None
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                continue
            sum = array[i] + array[j]
            sum = targetSum - sum
            
            if sum != array[i] and sum != array[j]:
                if sum in table:
                    val = [array[i], array[j], sum]
                    val.sort()
                    if tuple(val) in result_:
                        continue
                    result.append(val)
                    result_[tuple(val)] = None
    result.sort()
    return result
       
print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))