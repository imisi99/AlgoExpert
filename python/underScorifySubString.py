
# Time -> 0(N+M) Space -> 0(N)
def underscorifySubstring(string, substring):
    locations = []
    i = 0
    while i < len(string):
        val = string.find(substring, i)
        if val != -1:
            locations.append([val, val+len(substring)])
            i = val+1
        else:
            break

    if len(locations) == 0:
        return string
    
    newlocations = [locations[0]]
    for current in locations[1:]:
        last = newlocations[-1]
        
        if current[0] <= last[1]:
            last[1] = current[1]
        else:
            newlocations.append(current)

    print(newlocations, locations)
    
    newString = []
    i, j = 0, 0
    while i < len(string):
        if j < len(newlocations) and i == newlocations[j][0]:
            newString.append("_"+string[newlocations[j][0]:newlocations[j][1]]+"_")
            i = newlocations[j][1]
            j += 1
            continue
        else:
            newString.append(string[i])
        i += 1
            
    return "".join(newString)
    
print(underscorifySubstring("testtestesttestest this is a test to see if it works", "test"))