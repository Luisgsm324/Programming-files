class Heap:
    def __init__(self, array):
        self.array = array 
        self.size = len(self.array)

    def heapify(self, size,  i):
        biggest = i
        
        left = 2 * i + 1 
        right = 2 * i + 2 

        if left < size and self.array[i] < self.array[left]:
            biggest = left

        if right < size and self.array[biggest] < self.array[right]:
            biggest = right

        if biggest != i:
            self.array[i], self.array[biggest] = self.array[biggest], self.array[i] 
            #print(f"{self.array[-1]} ultimo elemento array")
            self.heapify(size, biggest)

    def heapsort(self):
        size = self.size

        for i in range(size // 2 - 1, -1, -1):
            self.heapify(size, i)


        for i in range(size - 1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i] # Swap
            break
            #self.heapify(i, 0)
        
        # O último elemento da array ordenada será o maior elemento.
        return self.array[-1]
    
    def multiple_maximums(self):
        self.heapsort()
        return self.array

question = input().split()
formated_list = []
for element in question:
    formated_list.append(int(element))

heap = Heap(formated_list)
print(heap.heapsort())
