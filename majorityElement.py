# Time: 0(n^2) Space: 0(1)
def majorityElement(array):
    max = 0
    element = 0
    for i in range(len(array)):
        count = 0
        for j in range(len(array)):
            if array[i] == array[j]:
                count += 1
        if count > max:
            max = count
            element = array[i]
    
    return element




# Time: 0(n) Space: 0(1)
def majorityElement(array):
    value = array[0]
    count = 1
    for i in range(1, len(array)):
        if count == 0:
            value = array[i]
        if array[i] == value:
            count += 1
        else:
            count -= 1
    return value

test = [1, 3, 2, 1, 2]
print(majorityElement(test))