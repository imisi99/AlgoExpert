# Time -> 0(N)   Space -> 0(N)
def sunsetViews(buildings, direction):
    max = 0
    result = []
    if direction == "EAST":
        start, stop = len(buildings) - 1, 0
        while start >= stop:
            if buildings[start] > max:
                result.append(start)
                max = buildings[start]
            start -= 1

        return result[::-1]
            
    else:
        start, stop = 0, len(buildings) - 1
        while start <= stop:
            if buildings[start] > max:
                result.append(start)
                max = buildings[start]
                
            start += 1
            
        return result
    
    
buildings = [3, 5, 4, 4, 3, 1, 3, 2]
print(sunsetViews(buildings, "EAST"))
print(sunsetViews(buildings, "WEST"))