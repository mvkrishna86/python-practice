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
            n = q.pop(0)
            print (n.data, end = " ")
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
    
    def print_all_paths(self, path, node):
        if not node:
            print(f"print_all_paths returning path: {path}")
            return path
        
        path.append(node.data)

        left_path = self.print_all_paths(list(path), node.left)
        right_path = self.print_all_paths(list(path), node.right)

        if len(left_path) > len(right_path):
            print(f"print_all_paths node: {node.data}, Path: {left_path}")
            return left_path
        else:
            print(f"print_all_paths node: {node.data}, Path: {right_path}")
            return right_path


    def find_longest_path(self, node, path=None):
        if path is None:
            path = []
        
        if not node:
            print(f"find_longest_path returning {path}")
            return path
        
        path.append(node.data)
        
        if not node.left and not node.right:
            print(f"find_longest_path node: {node.data}, Path: {path}")
            return path
        
        left_path = self.find_longest_path(node.left, path[:])
        right_path = self.find_longest_path(node.right, path[:])
        
        return left_path if len(left_path) > len(right_path) else right_path

    def print_longest_path1(self):
        longest_path = self.find_longest_path(self.root)
        print("Longest path from root to leaf:", longest_path)

        

tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(3)
tree.insert(1)
tree.insert(4)
tree.insert(15)
tree.insert(20)
tree.insert(30)
tree.insert(2)
tree.print_inorder(tree.root)
print("")
tree.level_order_traversal()
print("")
longest_path = tree.print_all_paths([], tree.root)
print(longest_path)
tree.print_longest_path1()
