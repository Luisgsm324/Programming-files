"""
Vamos construir uma classe que irá representar a nossa estrutura de dados, que seria a pilha.
"""

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

# Métodos importantes para que se tenha na pilha
# Inserir na pilha
# Remover na pilha 
# Observar o topo da pilha

# Node -> Nó
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem): # Inserir o elemento na pilha
        node = Node(elem)
        node.next = self.top # É necessário que conecte o Nó ao antigo topo
        self._size  += 1
        self.top = node

    def pop(self): # Remover o elemento do topo
        if self._size > 0:
            node = self.top
            self.top = self.top.next # Remove propriamente o elemento
            self._size  -= 1
            return node.data
        raise IndexError("A pilha está vazia")

    def peek(self): # Visualizar o topo da pilha
        if self._size > 0:
            return self.top.data
        raise IndexError("A pilha está vazia")
    
    def __repr__(self):
        r = ""
        pointer = self.top
        while pointer:
            r += str(pointer.data) + "\n"
            pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()
    