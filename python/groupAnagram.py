# Time -> 0(N*N*M) Space -> 0(N*W) where N = number of words and M = longest word
def groupAnagram(words: list) -> list:
    map = {}
    wordMap = {}
    wordsMap = {}
    initStore = []
    result = []
    
    for word in words:
        wordsMap[word] = False
    
    for word in words:
        map = {}
        initStore = []
        if wordsMap[word] == True:
            continue
        map = getMap(map, word)
        initStore.append(word)
        
        for newWord in words:
            if wordsMap[newWord] == True or newWord == word or len(newWord) != len(word):
                continue
            wordMap = {}
            wordMap = getMap(wordMap, newWord)
            if checkAnagram(map, wordMap):
                initStore.append(newWord)
                wordsMap[newWord] = True
                
        result.append(initStore)
        wordsMap[word] = True
    return result


def getMap(map: dict, word: str) -> dict:
    for char in word:
        map[char] = map.get(char, 0) + 1
    return map
        
        
def checkAnagram(firstMap: dict, secondMap: dict) -> bool:
    if len(firstMap) != len(secondMap):
        return False
    
    for k, v in firstMap.items():
        if k not in secondMap:
            return False
        val = secondMap[k]
        if val != v:
            return False
        
    return True


# Time -> 0(N*M log(M)) Space -> 0(MN)
def groupAnagram1(words: list) -> list:
    map = {}
    result = []
    for i in range(len(words)):
        word = sorted(words[i])
        word = ''.join(word)
        if word in map:
            map[word].append(words[i])
        else:
            map[word] = [words[i]]
    

    return list(map.values())
        
print(groupAnagram(["yo", "bro", "oy", "wrong", "cat","tac", "act"]))
print(groupAnagram1(["yo", "bro", "oy", "wrong", "cat", "tac", "act"]))