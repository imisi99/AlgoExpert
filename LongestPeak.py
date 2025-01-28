# Time: 0(n) Space: 0(1)
def longestPeak(array):
    peaks = 0
    l = 0
    n = len(array) - 1
    while l < n:
        peak_count = 0
        
   
        while l < n and array[l + 1] > array[l]:
            peak_count += 1
            l += 1
        if peak_count > 0:
            decreased = False
            while l < n and array[l + 1] < array[l]:
                peak_count += 1
                l += 1
                decreased = True
            if decreased:
                peak_count += 1
                if peak_count > peaks:
                    peaks = peak_count
                
        if peak_count == 0:
            l += 1
           
        
    return peaks
              


test = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
test1 = [1, 1, 2, 3, 1]
print(longestPeak(test))
