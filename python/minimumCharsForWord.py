# Time -> 0(N * M) Space -> 0(C) where N = len of words array , M = longest len of single word
#, and C = number of unique char 
def minimumChars(word: list) -> list:
    map = {}
    wordMap = {}
    result = []
    
    for val in word:
        wordMap = {}
        for char in val:
            wordMap[char] = wordMap.get(char, 0) + 1
        for k, v in wordMap.items():
            if k in map:
                map[k] = max(map[k], v)
            else:
                map[k] = v
                
    for k, v in map.items():
        for _ in range(v):
            result.append(k)
            
    return result


print(minimumChars(["this", "that", "did", "deed", "them!", "a"]))