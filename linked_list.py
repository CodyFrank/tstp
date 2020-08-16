class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def print_node(self):
        print(self.data)
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append_node(self, data):
        if not self.head:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def search(self, target):
        current = self.head
        while current != None:
            if current.data == target:
                print("Found it!")
                return True
            else:
                current = current.next
            print("Not found.")
            return False
