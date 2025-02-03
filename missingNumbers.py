# Time: 0(n) Space: 0(n)
def missingNumbers(nums):
    result = []
    store = set()
    for i in range(len(nums)):
        store.add(nums[i])
        
    n = len(nums)
    for i in range(1, n + 3):
        if i not in store:
            result.append(i)
            
    return result





# Time: 0(n(log(n))) Space: 0(1)
def missingNumbers(nums):
    n = len(nums) + 2
    result = []
    nums.sort()
    
    if len(nums) == 0:
        result.append(1)
        result.append(2)
        return result
    
    if nums[0] > 1:
        if nums[0] - 1 > 1:
            result.append(1)
            result.append(2)
        else:
            result.append(1)
    if len(result) != 2: 
        for i in range(n-3):
            if nums[i+1] - nums[i] > 2:
                val = nums[i+1] - 1
                result.append(val - 1)
                result.append(val)
                break
            if nums[i+1] - nums[i] > 1:
                result.append(nums[i+1] - 1)
        
    if n > nums[-1]:
        if n - nums[-1] > 1:
            result.append(n-1)
            result.append(n)
        else:
            result.append(n)
        
    return result


test = [1, 2, 7, 5, 4]

print(missingNumbers(test))