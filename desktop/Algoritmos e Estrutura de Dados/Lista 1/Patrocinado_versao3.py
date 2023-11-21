nomes = ["endrick", "neymar", "cr7", "messi"]
marcas = ["new balance", "puma", "nike" , "adidas"]

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Pilha:
    def __init__(self, lista):
        self.items = lista
        self.head = Node(lista[-1])
        self._size = len(lista)

    def analisePilha(self, nomes, marcas):
        nomes_array = []
        count = 0
        for item in self.items:
            if item in nomes:
                nomes_array.append(item)
            if item in marcas:
                if len(nomes_array) == 0:
                    return False
                if nomes.index(nomes_array[-1]) == marcas.index(item):
                    nomes_array.pop()
                    count += 1
        
        if count == (self._size)/2:
            return True
        return False

question = input().split("-")

pilha = Pilha(question)

if pilha.analisePilha(nomes, marcas):
    print("Correto")
else:
    print("Incorreto")

