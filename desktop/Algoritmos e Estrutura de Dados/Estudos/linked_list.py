class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None # Nessa situação seria None devido ao fato que a classe de linkedlist que estamos criando será vazia, porém nada impede que houvesse modificações que alterassem esse None (e será alterado)
        self._size = 0 # A lista é vazia, logo tem 0 elementos. O uso do _ antes do size, trata-se de uma convenção para quem estiver construindo uma aplicação compreender que não é um dado para ser acessado facilmente pelo usuário.

    def append(self, elem):
        elem = Node(elem)
        if self.head:
            pointer = self.head # Uma estrutura auxiliar que seria o ponteiro
            while pointer.next: # Vai parar quando for None e isso significa que o final da lista foi alcançado
                pointer = pointer.next
            pointer.next = elem  
        else:
            self.head = elem
        self._size += 1
    
    def __repr__(self): # Forma para fazer referência ao Node
        pointer = self.head
        nodes = []
        while pointer:
            nodes.append(str(pointer.data))
            pointer = pointer.next
        return "mapa:" + "->".join(nodes) 

    
    def __getitem__(self, index):
        pointer = self.head # Utilizar novamente a estrutura auxiliar 
        for _ in range(index):
            if pointer: #Verificar se o ponteiro não é None, ou seja, que a lista esteja vazia
                pointer = pointer.next
            else:
                raise IndexError("Index informado está fora do range da lista :(")
        if pointer:
            return pointer # Removi o .data para facilitar os comandos de empurrar e puxar
        raise IndexError("Index informado está fora do range da lista :(")
    
    def remove(self, node_to_remove): # Esse comando irá remover baseado no elemento, não na posição
        # Em situação que resolve logo, deixando a complexidade O(1) em vez de O(n)
        if self.head:
            if self.head.data == node_to_remove:
                self.head = self.head.next 
                return True
        
        pointer = self.head
        while pointer:
            if pointer.data == node_to_remove:
                break 
            prev = pointer
            pointer = pointer.next
        
        if pointer is None:
            return False # Implemetar aqui a parte de caso encontre um remove que não esteja 

        prev.next = pointer.next 
        pointer = None
        return True


    def insertAfter(self, before_node, new_data):
        new_node = Node(new_data) # Criou o nó com a nova informação
        new_node.next = before_node.next # O next da nova informação (o nó da nova informação) será o next do elemento anterior
        before_node.next = new_node # O next do elemento anterior será a nova informação (o nó da nova informação)
        

    def index(self, elem):
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError(f"O index {elem} não está na lista :(")

lista = LinkedList()

def main():
    while True:
        question = input()
        print(lista)
        if ":" in question:
            question_splitted = question.split(":")
            if question_splitted[1] == "adicione-me!":
                lista.append(question_splitted[0])
                print(f"Node {question_splitted[0]} adicionado")
            
            elif question_splitted[1] == "remova-me!":
                if lista.remove(question_splitted[0]):
                    print(f"Node {question_splitted[0]} foi removido")
                else:
                    print(f"Node {question_splitted[0]} não existe")
            
            elif question_splitted[1] == "empurre-me!":
                # Copiar
                try:
                    pos_targ = lista.index(question_splitted[0])
                    target_node = lista[pos_targ]
                    pos_before = pos_targ + 1
                    print(pos_before)
                    print(lista._size)
                    if pos_before == lista._size:
                        print(f"Não existe Node depois de {target_node.data}")
                    else:
                        before_node = lista[pos_before]
                        # Remover
                        lista.remove(target_node.data)

                        # Inserir
                        lista.insertAfter(before_node, target_node.data)
                        print(f"Node {question_splitted[0]} empurrado")
                        print(f"Tamanho da lista: {lista._size}")
                        if lista.index(question_splitted[0]) == lista._size:
                            lista._size += 1
                        
                except:
                    print(f"Node {question_splitted[0]} não existe")
            
            elif question_splitted[1] == "puxe-me!":
                try:
                    # Copiar
                    pos_targ = lista.index(question_splitted[0])
                    target_node = lista[pos_targ]
                    pos_before = pos_targ - 1
                    if pos_before == -1:
                        print(f"Não existe Node antes de {target_node.data}")
                    else:
                        before_node = lista[pos_before]
                        # Remover
                        lista.remove(before_node.data)
                        # Inserir
                        lista.insertAfter(target_node, before_node.data)
                        print(f"Node {question_splitted[0]} puxado")

                except:
                    print(f"Node {question_splitted[0]} não existe")
        else:
            break

main()

print(lista)