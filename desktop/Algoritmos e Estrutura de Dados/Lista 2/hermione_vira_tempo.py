class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None 
        self.height = 1 # Inclusão da altura como diferencial da árvore binária convencional 

class AVLtree:
    def insert(self, data, root): # Função de inserir na árvore AVL (vai pegar como parâmetro um valor desejado)
        if root is None:
            return Node(data)
        
        elif data < root.data:
            root.left = self.insert(data, root.left)

        else:
            root.right = self.insert(data, root.right)
        
        # Pegar a altura (será o maior entre a esquerda e a direita adicionando mais um)
        root.height = 1 + max(self.heightFunc(root.left), self.heightFunc(root.right))
        # Pegar o fator de "balanceamento" a fim de adequar as rotações que ocorrerão
        balance_factor = self.balanceFunc(root)

        # Rotações simples: 

        if balance_factor > 1 and data < root.left.data: # Direita
            return self.right_rotation(root)
        
        if balance_factor < -1 and data > root.right.data: # Esquerda
            return self.left_rotation(root)
        
        # Rotações duplas:

        if balance_factor > 1 and data > root.left.data:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)
        
        if balance_factor < -1 and data < root.right.data:
            root.right = self.right_rotation(root.right) 
            return self.left_rotation(root)

        return root


    def heightFunc(self, root):
        if root is None:
            return 0
        return root.height
    
    def balanceFunc(self, root):
        if root is None:
            return 0
        return self.heightFunc(root.left) - self.heightFunc(root.right)

    def right_rotation(self, refference):
        y = refference.left
        T3 = y.right

        y.right = refference
        refference.left = T3

        refference.height = 1 + max(self.heightFunc(refference.right), self.heightFunc(refference.left))
        y.height = 1 + max(self.heightFunc(y.right), self.heightFunc(y.left))

        return y
    
    def left_rotation(self, refference):
        y = refference.right
        T2 = y.left

        y.left = refference
        refference.right = T2

        refference.height = 1 + max(self.heightFunc(refference.right), self.heightFunc(refference.left))
        y.height = 1 + max(self.heightFunc(y.right), self.heightFunc(y.left))

        return y

    def descendingTree(self, biggests,  root): 
        if root is not None: 
            self.descendingTree(biggests,root.right) 
            biggests.append(root.data) 
            self.descendingTree(biggests,root.left) 
    
    def sum_biggests(self, limit, array):
        sum = 0 
        for index in range(limit):
            if index < len(array):
                sum += array[index]
            else:
                break
        return f"valor total de conhecimento: {sum}"

tree = AVLtree()
root = None

clas_quantify = input().split()

clas_hogwarts = input().split()
clas_cin = input().split()

clas_number = int(input())

clas_unified = clas_hogwarts + clas_cin

for element in clas_unified:
    root = tree.insert(int(element), root)

descen_numbers = []
variable = tree.descendingTree(descen_numbers, root)


print(tree.sum_biggests(clas_number, descen_numbers))
