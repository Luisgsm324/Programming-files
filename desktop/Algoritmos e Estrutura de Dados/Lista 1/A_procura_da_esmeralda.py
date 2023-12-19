class Node:
    def __init__(self, data):
        self.head = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAfter(self, before_node, new_data):
        new_node = Node(new_data) # Criou o nó com a nova informação
        new_node.next = before_node.next # O next da nova informação (o nó da nova informação) será o next do elemento anterior
        before_node.next = new_node # O next do elemento anterior será a nova informação (o nó da nova informação)
    
    def append(self, elem):
        elem = Node(elem)
        if self.head:
            pointer = self.head # Uma estrutura auxiliar que seria o ponteiro
            while pointer.next: # Vai parar quando for None e isso significa que o final da lista foi alcançado
                pointer = pointer.next
            pointer.next = elem  
        else:
            self.head = elem

    def remove(self, node_to_remove): # Esse comando irá remover baseado no elemento, não na posição
        # Em situação que resolve logo, deixando a complexidade O(1) em vez de O(n)
        if self.head:
            if self.head.data == node_to_remove:
                self.head = pointer.next 
                return
        pointer = self.head
        while pointer:
            if pointer.data == node_to_remove:
                break 
            prev = pointer
            pointer = pointer.next
        
        if pointer is None:
            return  # Implemetar aqui a parte de caso encontre um remove que não esteja 
        prev.next = pointer.next 
        pointer = None
    
    def moveRight(self, desired_node):
        pass 

lista = LinkedList()

def main():
    while True:
        question = input().split(":")
        if question[1] == "adicione-me!":
            lista.append(question[0])
            print(f"Node {question[0]} adicionado")

main()