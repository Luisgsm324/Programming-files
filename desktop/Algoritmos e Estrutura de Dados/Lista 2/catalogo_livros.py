class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None

class BinaryTree:
    def __init__(self,data=None):
        if data: 
            self.root = Node(data)
        else:
            self.root = None

    def insert(self, data):
        parent = None # Definir um "parente" com None como padrão 
        cur = self.root # Pegar a raiz como referência 
        while (cur): # Enquanto a raiz não for None, o loop continuará, percorrendo a árvore
            parent = cur
            if data < cur.data:
                cur = cur.left
            else:
                cur = cur.right

        # Se o elemento se tornar a raiz     
        if parent is None:
            self.root = Node(data)

        # Caso o valor dado for menor, ele estará na esquerda do nó 
        elif data < parent.data:  
            parent.left = Node(data)
        
        # Caso o valor dado for maior, ele estará na direita do nó (o else está funcionando levando em consideração o elemento estando na direita)
        else: # data > parent.data 
            parent.right = Node(data)

    def InOrder(self, node=None, lista=None):
        # O nó definido inicialmente como a raiz (pode funcionar colocando a raiz como parâmetro ou não)
        if node is None:
            node = self.root       
        
        # A busca em ordem irá buscar os elementos à esquerda, permitindo um processo recursivo para percorrer até que o node.left seja None
        if node.left:
            self.InOrder(node.left, lista)
        
        lista.append(node.data)
        
        if node.right:
            self.InOrder(node.right, lista)

tree = BinaryTree()

question = input().split()

for element in question:
    tree.insert(int(element))

lista = []
tree.InOrder(lista=lista)

for index in range(len(lista)):
    if index == len(lista) - 1:
        print(lista[index], end="")
    else:
        print(lista[index], end=" ")