# Time -> 0(ND) Space -> 0(N) where d is the denoms and n is the change
def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for _ in range(n+1)]
    
    ways[0] = 1
    
    for d in denoms:
        for i in range(len(ways)):
            if d <= i:
                ways[i] += ways[i-d]
    return ways[n]



print(numberOfWaysToMakeChange(6, [1, 5]))