class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        

def linkedListPalindrome(head):
    count = 0
    curr = head 
    
    while curr != None:
        count += 1
        curr = curr.next
        
    if count == 1:
        return True
    
    mid = count // 2
    if count % 2 == 1:
        mid += 1
        
    curr = head
    while mid > 0:
        curr = curr.next
        mid -= 1
        
    tail = None
    while curr != None:
        p1 = curr.next
        curr.next = tail 
        tail = curr
        curr = p1
    
    while tail != None:
        if tail.value != head.value:
            return False
        tail = tail.next
        head = head.next
        
    return True

array = [1, 2, 3, 2, 1, 0]
head = LinkedList(value=0)
curr = head
for val in array:
    curr.next = LinkedList(val)
    curr = curr.next
    
print(linkedListPalindrome(head))