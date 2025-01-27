# Time: 0(N^2) Space: 0(N)
def arrayOfProducts(array):
    result = []
    for i in range(len(array)):
        prod = 1
        for j in range(len(array)):
            if i == j:
                continue
            prod *= array[j]
        result.append(prod)
    return result

# Time: 0(N) Space: 0(N)
def arrayOfProducts(array):
    result = [1] * len(array)

    first = 1
    for i in range(len(array)):
        result[i] = first
        first *= array[i]
    first = 1
    for j in reversed(range(len(array))):
        result[j] *= first
        first *= array[j]
    return result

print(arrayOfProducts([5, 1, 4, 2]))