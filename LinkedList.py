class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def __init__(self, data = None):
        if data:
            n = Node(data)
            self.head = n
        else:
            self.head = None
    
    def insert_end(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = n

    def insert_beginning(self, data):
        n = Node(data)
        # if not self.head:
        #     self.head = n
        #     return
        n.next = self.head
        self.head = n
        
    
    def print(self):
        if not self.head:
            print("List is empty")
            return
        node = self.head
        while node:
            print (node.data, end = " ")
            node = node.next
        print("")


b = LinkedList()
b.insert_beginning(1)
b.insert_end(2)
b.insert_end(3)
b.insert_end(4)
b.insert_end(5)
b.insert_beginning(0)

b.print()