class Node:
    def __init__(self, data):
        self.data = data 
        self.prev = None # Nas estruturas anteriores, não tínhamos o armazenamento do Node anterior como temos na duplamente encadeada.
        self.next = None

class DoubleList:
    def __init__(self):
        self.head = None
    
    def push(self, data): # Adiciona no início
      elem = Node(data)
      elem.next = self.head
      if self.head is not None:
        self.head.prev = elem
      self.head = elem

    def remove(self, data):
        cur = self.head
        while (cur):
            # Situação geral que o elemento que queremos remover é o head da lista
            if cur.data == data and cur == self.head:
                # Situação que temos apenas um elemento na lista e este é o que queremos remover (a lista ficará vazia)
                if not cur.next: 
                    cur = None 
                    self.head = None
                    return
                # Situação que estamos removendo o primeiro elemento da lista, entretanto a lista não está ficando vazia
                self.head = self.head.next
                self.head.prev = None
                cur = None
                return
            
            elif cur.data == data:
                if cur.next: # Se não é o último elemento da lista
                    # Pegar as posições do próximo e do anterior
                    nxt = cur.next 
                    prev = cur.prev
                    
                    # Definir a posição do next do anterior como o posterior que estava ligado ao elemento entre eles e 
                    # Definir a posição do prev do posterior como o anterior que estava ligado ao elemento entre eles. 
                    prev.next = nxt 
                    nxt.prev = prev

                    # Remover completamente da lista após definir que ele não tem ligação posteriora ou anteriora
                    cur.next = None
                    cur.prev = None

                    # Finalizar o processo
                    cur = None 
                    return 
                
                prev = cur.prev
                prev.next = None

                cur.prev = None
                cur = None 
                return
            cur = cur.next

    def show_check_list(self):
        ref_list = []
        pointer = self.head
        while (pointer): # Irá parar até que o pointer seja None
            if pointer.data not in ref_list: # Se o nome já fora sido printado
                print(pointer.data)
                ref_list.append(pointer.data)
            pointer = pointer.next

doublelist = DoubleList()

while True:
    question = input().split()
    if "deixou" not in question and "fechou" not in question:
        
        doublelist.push(question[-1])
    
    elif "deixou" in question:
        doublelist.remove(question[-1])
    
    else:
        break

doublelist.show_check_list()