class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        

def zipLinkedList(head):
    count = 0
    
    curr = head
    
    while curr != None:
        count += 1
        curr = curr.next
    
    if count == 1:
        return head
    
    startNorm, endNorm = None, None
    
    mid = 0
    if count % 2 == 0:
        mid = count / 2
    else:
        mid = (count // 2 ) + 1
    
    while mid > 0:
        if startNorm == None:
            startNorm = head
            endNorm = startNorm
            mid -= 1
        else:
            endNorm = endNorm.next
            mid -= 1
    
    startZip, endZip = None, endNorm.next
    
    while endZip != None:
        point = endZip.next
        endZip.next = startZip
        startZip = endZip
        endZip = point
        
    endNorm.next = None
    
    zippedList, zippedHead = None, None
    
    while startNorm != None:
        if zippedList == None:
            zippedList = startNorm
            zippedHead = zippedList
            startNorm = startNorm.next
            zippedList.next = startZip
            startZip = startZip.next
            zippedList = zippedList.next
    
        else:
            zippedList.next = startNorm
            startNorm = startNorm.next
            zippedList = zippedList.next
            if startZip == None:
                break
            zippedList.next = startZip
            startZip = startZip.next
            zippedList = zippedList.next
      
    return zippedHead


head = LinkedList(0)
curr = head
array = [3, 0, 5, 2, 1, 4]

for val in range(len(array)):
    curr.value = array[val]
    if val == len(array) - 1:
        break
    curr.next = LinkedList(0)
    curr = curr.next
    
arrange = zipLinkedList(head)

while arrange != None:
    print(arrange.value, end="->")
    arrange = arrange.next
print()