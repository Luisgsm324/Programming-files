class Heap:
    def __init__(self, array):
        self.array = array 
        self.size = len(self.array)

    def heapify(self, n,  i):
        biggest = i
        l = 2 * i + 1 # Esquerda (l de left)
        r = 2 * i + 2 # Direita (r de right)

        if l < n and self.array[i] < self.array[l]:
            biggest = l

        if r < n and self.array[biggest] < self.array[r]:
            biggest = r

        if biggest != i:
            self.array[i], self.array[biggest] = self.array[biggest], self.array[i]
            self.heapify(n, biggest)

    def heapsort(self):
        n = self.size

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heapify(i, 0)

    def multiple_maximums(self):
        self.heapsort()
        return self.array[-1] * self.array[-2]

question = input().split(",")
formated_list = []
for element in question:
    formated_list.append(int(element))

heap = Heap(formated_list)

result = heap.multiple_maximums()
print(f"R${result}")