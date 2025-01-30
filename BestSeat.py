def bestSeat(seats):
    n = len(seats) - 2
    i = 1
    while i <= n:
        if seats[i-1] == 0 and seats[i] == 0 and seats[i+1] == 0:
            return i
        i += 1
    i = 1
    while i <= n:
        if seats[i] == 0 and seats[i+1] == 0:
            return i
        i += 1
    i = 1
    while i <= n:
        if seats[i] == 0:
            return i
        i += 1
        
    return -1

test = [1, 0, 1]

print(bestSeat(test))