class MaxHeap:
    def __init__(self, array):
        self.heap = array
    
    def buildHeap(self):
        startIdx = (len(self.heap)-2) // 2
        while startIdx >= 0:
            self.siftDown(startIdx, len(self.heap)-1)
            startIdx -= 1
            
        print("After Initial Build -> ", self.heap)
            
    def biggest(self, x, y):
        if self.heap[x] >= self.heap[y]:
            return x
        return y
    
    def remove(self, window):
        endIdx = len(self.heap) - window - 1
        self.heap[0], self.heap[endIdx] = self.heap[endIdx], self.heap[0]
        self.siftDown(0, endIdx-1)
        
    def siftDown(self, startIdx, endIdx):
        while startIdx < endIdx:
            firstChild, secondChild = (startIdx * 2) + 1, (startIdx * 2) + 2
            if firstChild > endIdx:
                break
            biggest = 0
            if secondChild <= endIdx:
                biggest = self.biggest(firstChild, secondChild)
            else:
                biggest = firstChild
                
            if self.heap[biggest] > self.heap[startIdx]:
                self.heap[biggest], self.heap[startIdx] = self.heap[startIdx], self.heap[biggest]
                startIdx = biggest
            else:
                break
            
     
# Time -> 0(N(log(N))) Space -> 0(1) 
def heapSort(array):
    heap = MaxHeap(array)
    heap.buildHeap()
    idx = 0
    
    while idx < len(array) - 1:
        heap.remove(idx)
        idx += 1
        
    return array

print(heapSort([8, 5, 2, 9, 5, 6, 3]))