class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        

# Time -> 0(N) Space -> 0(1)
def nodeSwap(head):
    swap = head
    
    while swap != None:
        if swap.next == None:
            break
        swap.value, swap.next.value = swap.next.value, swap.value
        swap = swap.next.next 
    
    return head


head = LinkedList(0)
curr = head
array = [3, 0, 5, 2, 1]

for val in range(len(array)):
    curr.value = array[val]
    if val == len(array) - 1:
        break
    curr.next = LinkedList(0)
    curr = curr.next
    
arrange = nodeSwap(head)

while arrange != None:
    print(arrange.value, end=" -> ")
    arrange = arrange.next
print()