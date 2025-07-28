word = "Algoexpert is the best! 😊"


# Time -> 0(N) Space -> 0(N)
def ReverseWords(word: str) -> str:
    reversed_words = []
    end = len(word)-1
    i = end
    while i >= 0:
        if i == 0:
            reversed_words.append(word[i:end+1])
            break
        if word[i] == " ":
            if end > i:
                reversed_words.append(word[i+1:end+1])
            reversed_words.append(" ")
            end = i-1
        i -= 1
            
    return "".join(reversed_words)


print(ReverseWords(word=word))