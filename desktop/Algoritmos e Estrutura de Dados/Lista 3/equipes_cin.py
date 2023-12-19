class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None # Nessa situação seria None devido ao fato que a classe de linkedlist que estamos criando será vazia, porém nada impede que houvesse modificações que alterassem esse None (e será alterado)

    def append(self, elem):
        elem = Node(elem)
        if self.head:
            pointer = self.head # Uma estrutura auxiliar que seria o ponteiro
            while pointer.next: # Vai parar quando for None e isso significa que o final da lista foi alcançado
                pointer = pointer.next
            pointer.next = elem  
        else:
            self.head = elem

    def sortList(self):    
        cur = self.head 
        index = None 
        while(cur):  
            index = cur.next  
                  
            while(index):  
                if cur.data > index.data:  
                    temp = cur.data  
                    cur.data = index.data  
                    index.data = temp  
                index = index.next  
            cur = cur.next 
    
    def display(self, return_list, size):  
        prov_list = []
        count = 0
        current = self.head   
        while(current != None):  
            if count >= size:
                return_list.append(prov_list)
                count = 0
                prov_list = []
            prov_list.append(current.data)
            count += 1  
            current = current.next 
        if len(prov_list) != 0:
            return_list.append(prov_list)
        return return_list

groups = []

for _ in range(10):
    groups.append(LinkedList())

while True:
    try:
      question = input().split() # O primeiro elemento corresponde ao nome e o segundo ao tamanho do grupo
      groups[int(question[1]) -1].append(question[0])
    except:
        break

return_list = [] 
for linkedlist in groups:
    if linkedlist.head is not None:
        size = groups.index(linkedlist) + 1
        prov_list = []
        count = 0
        linkedlist.sortList()
        linkedlist.display(return_list, size)

print(return_list)