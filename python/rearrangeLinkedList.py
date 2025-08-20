class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        

# Time -> 0(N) Space -> 0(1)
def rearrangeLinkedList(head: LinkedList, k: int):
    newHead, less, startMerge, endMerge, startGreat, great = None, None, None, None, None, None
    
    curr = head
    while curr != None:
        if curr.value < k:
            if newHead == None:
                newHead = curr
                less = newHead
            else:
                less.next = curr
                less = less.next
        elif curr.value > k:
            if startGreat == None:
                startGreat = curr
                great = startGreat
            else:
                great.next = curr
                great = great.next
        else:
            if startMerge == None:
                startMerge = curr
                endMerge = startMerge
            else:
                endMerge.next = curr
                endMerge = endMerge.next
                
        curr = curr.next
        
    if newHead == None or startGreat == None or startMerge == None:
        if newHead == None:
            if startMerge == None:
                return startGreat
            else:
                if startGreat == None:
                    return startMerge
                else:
                    endMerge.next = startGreat
                    great.next = None
                    return startMerge
            
        else:
            if startMerge == None:
                if startGreat == None:
                    return newHead
                else:
                    less.next = startGreat
                    great.next = None
                    return newHead
            else:
                less.next = startMerge
                endMerge.next = None
                return newHead

                    
    less.next = startMerge
    endMerge.next = startGreat
    great.next = None
    
    return newHead

head = LinkedList(0)
curr = head
array = [3, 0, 5, 2, 1, 4]

for val in range(len(array)):
    curr.value = array[val]
    if val == len(array) - 1:
        break
    curr.next = LinkedList(0)
    curr = curr.next
    
arrange = rearrangeLinkedList(head, 3)

while arrange != None:
    print(arrange.value, end="->")
    arrange = arrange.next
print()