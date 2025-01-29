# Time: 0(N) Space: 0(N)
def mergeOverlappingIntervals(intervals):
    result = []
    n = len(intervals) - 1
    i = 0
    intervals.sort()
    while i <= n:
        # Last element 
        if i == n:
            result.append(intervals[i])
            break
        if intervals[i][1] < intervals[i + 1][0]:
            result.append(intervals[i])
            i += 1
        else:
            start = float("-inf")
            while i < n and intervals[i][1] >= intervals[i + 1][0]:
                if start == float("-inf"):
                    start = intervals[i][0]
                i += 1
            end = intervals[i][1]
            result.append([start, end])
            i += 1
            
    return result



test = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]

print(mergeOverlappingIntervals(test))