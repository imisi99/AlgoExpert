# Time: 0(N) Space: 0(1)
def isMonotonic(array):
    n = len(array) - 1
    if n == -1 or n == 0:
        return True
    dir = "increasing" if array[n] > array[0] else "decreasing"
    if dir == "decreasing":
        for i in range(n):
            if array[i + 1] > array[i]:
                return False
    else:
        for i in range(n):
            if array[i + 1] < array[i]:
                return False
    return True

test = [-1, -5, -10, -1100, -1101, -1102, -9001]
print(isMonotonic(test))