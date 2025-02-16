# Time: 0(m * n) Space: 0(1)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    current = linkedListOne
    
    while current:
        current1 = linkedListTwo
        while current1:
            if current.value == current1.value:
                return current
            current1 = current1.next
        current = current.next
        
    return None
