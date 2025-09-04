def longestPalindrome(string: str) -> str:
    longest, startIdx, stopIdx = 0, 0, 0
    for i in range(1, len(string)):
        length, start, stop = checkPalindrome(string, i-1, i+1)
        length1, start1, stop1 = checkPalindrome(string, i-1, i)
        if length > longest:
            longest = length
            startIdx, stopIdx = start, stop
        elif length1 > longest:
            longest = length1
            startIdx, stopIdx = start1, stop1
    return string[startIdx:stopIdx+1]


def checkPalindrome(string: str, i: int, j: int) -> tuple:
    while i >= 0 and j < len(string) and string[i] == string[j]:
        i -= 1
        j += 1   
    return j-i-1, i+1, j-1
        
    
        
print(longestPalindrome("abaxyzzyxfxxxxxxx"))