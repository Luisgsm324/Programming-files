jogadores_info = {
    "endrick": "new balance",
    "messi": "adidas",
    "cr7": "nike",
    "neymar": "puma"
}


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Pilha:
    def __init__(self, lista):
        self.head = Node(lista[-1])
        self.size = len(lista)
    
    def analisePilha(self, lista_input, jogadores_info):
        count = 0
        if self.size % 2 == 0:
            for index1 in range(len(lista_input) - 1):
                for index2 in range(len(lista_input) - 1):
                    if jogadores_info.get(lista_input[index2]) == lista_input[index1 + 1]:
                        count += 1
            if count == self.size/2:
                return True 
            return False
        return False

question = input().split("-")

pilha = Pilha(question)

if pilha.analisePilha(question, jogadores_info):
    print("Correto")
else:
    print("Incorreto")
