class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
class BinaryTree:

    def __init__(self):
        self.root = None
    
    def insert(self, data):
        node = Node(data)

        if self.root == None:
            self.root = node
        else:
            temp = self.root
            while True:
                if data < temp.data:
                    if temp.left == None:
                        temp.left = node
                        return
                    temp = temp.left;
                else:
                    if temp.right == None:
                        temp.right = node
                        return
                    temp = temp.right
    

    def print_inorder(self, node):
        if node == None:
            return
        self.print_inorder(node.left)
        print(node.data, end = " ")
        self.print_inorder(node.right)


    def level_order_traversal(self):
        if not self.root:
            return
        q = []
        node = self.root
        q.append(node)

        while len(q) > 0:
            n = q.pop()
            print (n.data, end = " ")
            if not n.left:
                q.append(n.left)
            if not n.right:
                q.append(n.right)
        

tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(3)
tree.insert(1)
tree.insert(4)
tree.insert(15)
tree.insert(20)
tree.insert(30)
tree.print_inorder(tree.root)
print("")
tree.level_order_traversal()

            