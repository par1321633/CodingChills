class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, data):
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data, current)

    def prepend(self, data):
        current = self.head
        node = Node(data, next=current)
        current.prev = node
        self.head = node

    def add_item_after(self, item, value):
        current = self.head
        if current is None:
            return
        while current:
            current = current.next
            if current is None:
                break
            if current.data == item:
                node = Node(value)
                node.prev = current
                node.next = current.next
                current.next.prev = node
                current.next = node
                break

    def get_all_nodes(self):
        current = self.head
        if current is None:
            return
        while current:
            print(current.data, end=" ")
            if current.next is not None:
                print (" ", end="-> ")
            current = current.next

    def get_all_nodes_reverse(self):
        current = self.head
        if current is None:
            return
        while current:
            current = current.next
            if current.next is None:
                last_item = current
                break

        while last_item:
            print(last_item.data)
            last_item = last_item.prev
            if last_item is None:
                break

    def delete_node(self, node):
        current = self.head
        while current:
            if current.data == node:
                current.next.prev = current.prev
                current.prev.next = current.next
                break
            if current.next is None:
                print ("Item Not Found")
            current = current.next