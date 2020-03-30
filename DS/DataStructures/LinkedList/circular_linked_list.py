class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self,head):
        self.head = head
        self.head.next = self.head

    def append(self,data):
        current = self.head
        while current.next:
            if current.next == self.head:
                node = Node(data)
                current.next = node
                node.next = self.head
                break
            current = current.next

    def prepend(self, data):
        current = self.head
        while current.next:
            if current.next == self.head:
                node = Node(data)
                current.next = node
                node.next = self.head
                self.head = node
                break
            current = current.next

    def get_all_nodes(self):
        current = self.head
        if current is None:
            return
        while current:
            print (current.data)
            if current.next == self.head:
                break
            current = current.next

    def add_after(self, data, after):
        current = self.head
        if current is None:
            return
        while current:
            if current.data == after:
                req_node = Node(data)
                req_node.next = current.next
                current.next = req_node
                break
            else:
                current = current.next

    def add_before(self, data, before):
        current = self.head
        if current is None:
            return

        if current.data == before:
            self.prepend(data)
            return

        while current:
            if current.next is None:
                self.append(data)
                return
            if current.next.data == before:
                req_node = Node(data)
                req_node.next = current.next
                current.next = req_node
                break
            else:
                current = current.next

    def update_node(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                break
            current = current.next

    def delete_node(self, data):
        current = self.head
        if current.data == data:
            while current:
                if current.next == self.head:
                    self.head = current.next.next
                    current.next = self.head
                    break
                current = current.next
            return

        while current:
            if current.next is None:
                print ("Data is Not Present in LinkedList")
                return
            if current.next.data == data:
                current.next = current.next.next
                break
            current = current.next

"""
node = Node(10)
ll = CircularLinkedList(node)
print ("Ciruclar LinkedList")
ll.get_all_nodes()

print ("Append Node 20")
ll.append(20)
ll.get_all_nodes()

print ("Prepend Node 1")
ll.prepend(1)
ll.get_all_nodes()

print ("Append Node 8")
ll.append(8)
ll.get_all_nodes()

print ("Append Node 12 after 20")
ll.add_after(12,20)
ll.get_all_nodes()

print ("Append Node 11 before 20")
ll.add_before(11,20)
ll.get_all_nodes()

print ("Delete Node 1")
ll.delete_node(1)
ll.get_all_nodes()

print ("Delete Node 2")
ll.delete_node(2)
ll.get_all_nodes()
"""
