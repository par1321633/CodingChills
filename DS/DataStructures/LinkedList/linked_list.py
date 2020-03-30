class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, data):
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def prepend(self, data):
        current = self.head
        node = Node(data)
        self.head = node
        node.next = current

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
            self.prepend(before)
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

    def get_all_nodes(self):
        current = self.head
        if current is None:
            return
        while current:
            print(current.data)
            current = current.next
            if current is None:
                break

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
            self.head = current.next
            return

        while current:
            if current.next is None:
                print ("Data is Not Present in LinkedList")
                return

            if current.next.data == data:
                current.next = current.next.next
                break
            current = current.next

node = Node(10)
ll = LinkedList(node)

ll.get_all_nodes()


ll.append(17)
ll.prepend(2)
ll.add_after(4, 10)
ll.add_before(3, 10)
ll.add_before(12,20)
ll.get_all_nodes()

ll.delete_node(2)
ll.get_all_nodes()

ll.update_node(30,100)
ll.get_all_nodes()