class MinHeap:
    def __init__(self):
        self.heap = []
        
    def __len__(self):
        return len(self.heap)
    
    def peek(self):
        return self.heap[0]
    
    def siftup(self):
        lastIdx = len(self.heap) - 1
        while lastIdx >= 1:
            parent = (lastIdx - 1) // 2
            if self.heap[lastIdx] < self.heap[parent]:
                self.heap[lastIdx], self.heap[parent] = self.heap[parent], self.heap[lastIdx]
                lastIdx = parent
            else:
                break
            
    def smallest(self, x, y):
        if self.heap[x] <= self.heap[y]:
            return x
        return y
    
    def siftdown(self):
        startIdx, endIdx = 0, len(self.heap) - 1 
        while startIdx < endIdx:
            firstChild, secondChild = (startIdx * 2) + 1, (startIdx * 2) + 2
            if firstChild > endIdx:
                break
            smallest = 0
            if secondChild <= endIdx:
                smallest = self.smallest(firstChild, secondChild)
            else:
                smallest = firstChild
            
            if self.heap[smallest] < self.heap[startIdx]:
                self.heap[smallest], self.heap[startIdx] = self.heap[startIdx], self.heap[smallest]
                startIdx = smallest
            else: 
                break
    
    def remove(self):
        last = len(self.heap) - 1
        self.heap[0], self.heap[last] = self.heap[last], self.heap[0]
        self.heap.pop()
        self.siftdown()
        
    def insert(self, val):
        self.heap.append(val)
        self.siftup()
        

# Time -> 0(N log(N)) Space -> 0(N)
def laptopRentals(times):
    times.sort(key=lambda x: (x[0], x[1]))
    heap = MinHeap()
    num = 0
    for i in range(len(times)):
        if len(heap) == 0:
            num += 1
            heap.insert(times[i][1])
            continue
        
        if times[i][0] >= heap.peek():
            heap.remove()
            heap.insert(times[i][1])
        else:
            num += 1
            heap.insert(times[i][1])
            
    return num

print(laptopRentals([[1, 4], [0, 4], [0, 2], [4, 6], [7, 8], [3, 10], [9, 11]]))