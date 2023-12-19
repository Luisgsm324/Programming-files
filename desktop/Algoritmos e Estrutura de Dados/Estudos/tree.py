from fila import Queue

ROOT = "root"
class Node:
    def __init__(self, data):
        self.data = data
        # Os dois atributos abaixos referenciam-se ao filho à direita e à esquerda
        self.left = None 
        self.right = None 
    
    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        
        if node.left:
            print("(", end="")
            self.simetric_traversal(node.left)
        print(node.left, end="")

        if node.right:
            self.simetric_traversal(node.right)
            print(")", end="")
    
    def postorder_traversal(self, node=None):
        # O percurso em pós-ordem vai buscar todos os elementos a esquerda, em seguida a direita para enfim printar a si mesmo
        if node is None:
            node = self.root

        # Por meio de recursão é navegado os elementos a esquerda (ocorre um loop recursivo, sendo o caso base quando node.left == None)
        if node.left:
            self.postorder_traversal(node.left)
        # Mesmo processo ocorrido anteriormente na esquerda
        if node.right:
            self.postorder_traversal(node.right)
        # Quando enfim não se tem mais nada a esquerda que foi visualizado ou a direita, o elemento é printado
        print(node)

    def height(self, node=None):
        # O percurso em pós-ordem vai buscar todos os elementos a esquerda, em seguida a direita para enfim printar a si mesmo
        if node is None:
            node = self.root

        hleft = 0
        hright = 0
        # Por meio de recursão é navegado os elementos a esquerda (ocorre um loop recursivo, sendo o caso base quando node.left == None)
        if node.left:
            hleft = self.height(node.left)
        # Mesmo processo ocorrido anteriormente na esquerda
        if node.right:
            hright = self.height(node.right)
        
        if hright > hleft:
            return hright + 1 
        return hleft + 1

    def levelorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root

        queue = Queue()
        queue.push(node)
        while len(queue):
            node = queue.pop()
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
            print(node, end=" ")


# Uma árvore binária de busca pegando como herança a árvore binária construída anteriormente
class BinarySearchTree(BinaryTree):
    def insert(self, data):
        parent = None 
        cur = self.root # Coloca como referência a raiz da árvore
        while (cur): # Enquanto não for None
            parent = cur # Coloca o parent como o referência
            
            # Vai percorrendo até que cur seja None
            if data < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        
        if parent is None:
            self.root = Node(data)

        elif data < parent.data: # Seguindo as regras, o que vem a esquerda é o menor
            parent.left = Node(data)
        
        # Então, o que virá a direita, será o maior
        else: # data > parent.data 
            parent.right = Node(data)
    
    def search(self, data):
        return self._search(data, self.root)

    def _search(self, data, node):
        if node is None or node.data == data:
            return BinarySearchTree(node)
        
        if data < node.data:
            return self._search(data, node.left)
        return self._search(data, node.right)
    
    def inorder(self, node=None):
        if node is None:
            node = self.root       
        if node.left:
            self.inorder(node.left)
        print(node, end=" ")
        if node.right:
            self.inorder(node.right)



tree = BinarySearchTree()


question = input().split()
print(question)

for element in question:
    tree.insert(int(element))

tree.levelorder_traversal()