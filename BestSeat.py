# Time: 0(n) Space: 0(n)
def bestSeat(seats):
    table = {}
    i = 1
    n = len(seats) - 2
    
#     # get all the positions of the available seats
    while i <= n:
        count = 0
        if seats[i] == 0:
            while seats[i] == 0:
                count += 1
                i += 1
            table[i] = count
        else:
            i += 1
        
#     # get the one with the best space sitting
    count = 0
    end = 0
    for key, val in table.items():
        if val > count:
            count = val
            end = key
            
    if len(table) != 0:
        if count % 2 == 0:
            start = end - count
            return (start + (count // 2)) - 1
        else:
            start = end - count
            return (start + (count // 2))
    return -1




# Time: 0(n) Space: 0(1)
def bestSeat(seats):
    f_count = 0
    end = 0
    i = 1
    n = len(seats) - 2
    
    # get the place with the highest available consecutive space
    while i <= n:
        count = 0
        if seats[i] == 0:
            while seats[i] == 0:
                count += 1
                i += 1
            if count > f_count:
                f_count = count
                end = i 
        else:
            i += 1
        
    # get the best position with space on both sides 
    if f_count > 0:
        if f_count % 2 == 0:
            start = end - f_count
            return (start + (f_count // 2)) - 1
        else:
            start = end - f_count
            return (start + (f_count // 2))
    return -1



test = [1, 0, 0, 1, 0, 0, 0, 1]
test1 = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]

print(bestSeat(test1))