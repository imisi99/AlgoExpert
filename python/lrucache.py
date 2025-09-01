class LinkedList:
    def __init__(self, key, value):
        self.next = None
        self.prev = None
        self.key = key
        self.value = value
        

class LRUCache:
    def __init__(self, maxsize):
        self.maxsize = maxsize or 1
        self.currsize = 0
        self.cache = {}
        self.head = None
        self.tail = None
  
    # Time -> 0(1) Space -> 0(1)
    def insertKeyValuePair(self, key, value):
        if key in self.cache:
            pointer = self.cache[key]
            pointer.value = value
            return
        if self.currsize == self.maxsize:
            self.deleteKey()
        pointer = LinkedList(key=key, value=value)
        self.cache[key] = pointer
        self.currsize = min(self.currsize+1, self.maxsize)
        if self.head == None:
            self.head = pointer
            self.tail = pointer
            return
        pointer.prev = self.tail
        self.tail.next = pointer
        self.tail = pointer
        
    # Time -> 0(1) Space -> 0(1)   
    def getValueFromKey(self, key):
        if key in self.cache:
            pointer = self.cache[key]
            self.updateRecentlyUsedKey(pointer)
            return pointer.value
        return None
    
    # Time -> 0(1) Space -> 0(1)
    def getMostRecentKey(self):
        if self.currsize == 0:
            return None
        return self.tail.key
    
    
    def updateRecentlyUsedKey(self, pointer):
        if pointer == self.tail:
            return
        elif pointer == self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            pointer.next.prev = pointer.prev
            pointer.prev.next = pointer.next
            
        pointer.prev = self.tail
        self.tail.next = pointer
        self.tail = pointer
        self.tail.next = None
        
    
    def deleteKey(self):
        key = self.head.key
        self.head = self.head.next
        if self.head != None:
            self.head.prev = None
        self.cache.pop(key)
        
        
lru = LRUCache(maxsize=4)
lru.insertKeyValuePair("a", 1)
lru.insertKeyValuePair("b", 2)
print(lru.getMostRecentKey())
print(lru.getValueFromKey("a"))
lru.insertKeyValuePair("c", 3)
print(lru.getValueFromKey("d"))
lru.insertKeyValuePair("d", 4)
lru.getValueFromKey("b")
