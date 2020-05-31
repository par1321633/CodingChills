class Node:

    def __init__(self, data):
        self.data = data
        self.height = 0  # -- New Parameter, for Node it will 0 (Leaf Node)
        self.leftChild = None
        self.rightChild = None


class AVL(object):
    def __init__(self):
        self.root = None

    ### HELPER MEthods####
    def calcheight(self, node):
        if node is None:
            return -1
        return node.height

    def calcbalance(self, node):
        # if it return value > 1 it means left heavy tree - right rotation
        # value < -1 right heavy tree -- left rotation
        if not node:
            return 0
        return self.calcheight(node.leftChild) - self.calcheight(node.rightChild)

    def rotate_right(self, node):
        print ("Rotating RIGHT at Node :{}".format(node.data))
        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node
        node.leftChild = t

        node.height = max(self.calcheight(node.leftChild), self.calcheight(node.rightChild)) + 1
        tempLeftChild.height = max(self.calcheight(tempLeftChild.leftChild),
                                   self.calcheight(tempLeftChild.rightChild)) + 1
        return tempLeftChild

    def rotate_left(self, node):
        print ("Rotating LEFT at Node :{}".format(node.data))
        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        tempRightChild.leftChild = node
        node.rightChild = t

        node.height = max(self.calcheight(node.leftChild), self.calcheight(node.rightChild)) + 1
        tempRightChild.height = max(self.calcheight(tempRightChild.leftChild),
                                    self.calcheight(tempRightChild.rightChild)) + 1
        return tempRightChild

    def traverseInorder(self):
        if self.root:
            self.traverseInOrderRecur(self.root)
        else:
            print ("Tree is empty")

    def traverseInOrderRecur(self, node):
        if node.leftChild is not None:
            self.traverseInOrderRecur(node.leftChild)

        print (node.data)

        if node.rightChild is not None:
            self.traverseInOrderRecur(node.rightChild)

    def insert(self, data):
        self.root = self.insertNode(self.root, data)

    def insertNode(self, node, data):
        if node is None:
            return Node(data)
        if node.data > data:
            print ("Node is greater than data : {} > {}".format(node.data, data))
            node.leftChild = self.insertNode(node.leftChild, data)
        else:
            print ("Node is smaller than data : {} < {}".format(node.data, data))
            node.rightChild = self.insertNode(node.rightChild, data)
        node.height = max(self.calcheight(node.leftChild), self.calcheight(node.rightChild)) + 1
        print (self.traverseInorder())
        # print (node)
        # print (node.rightChild.data)
        # print (node.rightChild.rightChild)
        # return node
        return self.settleViolation(data, node)

    def settleViolation(self, data, node):
        balance = self.calcbalance(node)

        if balance > 1 and data < node.leftChild.data:
            print ("LEFT LEFT HEAVY")
            return self.rotate_right(node)

        if balance < -1 and data > node.rightChild.data:
            print ("RIGHT RIGHT HEAVY")
            return self.rotate_left(node)

        if balance > 1 and data > node.leftChild.data:
            print ("LEFT RIGHT HEAVY")
            node.leftChild = self.rotate_left(node.leftChild)
            return self.rotate_right(node)

        if balance < -1 and data < node.rightChild.data:
            print ("RIGHT LEFT HEAVY")
            print (node.data)
            node.rightChild = self.rotate_right(node.rightChild)
            return self.rotate_left(node)
        return node

    def removeData(self, data):
        if self.root:
            self.root = self.removeNode(self.root, data)

    def removeNode(self, node, data):
        print ("Data to delete : {}".format(data))
        if not node:
            return node
        if node.data > data:
            node.leftChild = self.removeNode(node.leftChild, data)
        elif node.data < data:
            node.rightChild = self.removeNode(node.rightChild, data)
        else:
            if node.leftChild is None and node.rightChild is None:
                print ("Leaf Node")
                del node
                return None
            elif node.leftChild is None:
                print ("Removing Node with right Child")
                tempNode = node.rightChild
                del node
                return tempNode
            elif node.rightChild is None:
                print ("Removing Node with left Child")
                tempNode = node.leftChild
                del node
                return tempNode
            print (node.data)
            print (node.leftChild.data)
            print ("Removing Node with 2 Children")
            tempNode = self.getPredeccor(node.leftChild)
            print (self.traverseInorder())
            node.data = tempNode.data
            print (self.traverseInorder())
            node.leftChild = self.removeNode(node.leftChild, tempNode.data)
            print (self.traverseInorder())

        if not node:
            return node

        node.height = max(self.calcheight(node.leftChild), self.calcheight(node.rightChild)) + 1
        print (node.data)
        print (node.height)
        balance = self.calcbalance(node)
        print (balance)
        print (self.calcbalance(node.leftChild))
        print (self.calcbalance(node.rightChild))
        print ("!!!!!!!")
        if balance > 1 and self.calcbalance(node.leftChild) >= 0:
            print ("LEFT LEFT HEAVY")
            return self.rotate_right(node)

        if balance > 1 and self.calcbalance(node.leftChild) < 0:
            print ("LEFT RIGHT HEAVY")
            node.leftChild = self.rotate_left(node.leftChild)
            return self.rotate_right(node)

        if balance < -1 and self.calcbalance(node.rightChild) <= 0:
            print ("RIGHT RIGHT HEAVY")
            return self.rotate_left(node)

        if balance < -1 and self.calcbalance(node.rightChild) > 0:
            print ("RIGHT LEFT HEAVY")
            print (node.data)
            node.rightChild = self.rotate_right(node.rightChild)
            return self.rotate_left(node)
        return node


def run_left_heavy_case():
    print (" ============= RUNNING LEFT LEFT CASE ================= ")
    avl = AVL()
    avl.insert(5)
    avl.insert(4)
    avl.insert(3)
    avl.insert(2)
    avl.insert(1)
    avl.traverseInorder()

def run_right_heavy_case():
    print (" ============= RUNNING RIGHT RIGHT CASE ================= ")
    avl = AVL()
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    avl.insert(40)
    avl.insert(50)
    avl.traverseInorder()

def run_left_right_case():
    print (" ============= RUNNING LEFT RIGHT CASE ================= ")
    avl = AVL()
    avl.insert(5)
    avl.insert(3)
    avl.insert(4)
    avl.traverseInorder()

def run_right_left_case():
    print (" ============= RUNNING RIGHT LEFT CASE ================= ")
    avl = AVL()
    avl.insert(10)
    avl.insert(20)
    avl.insert(15)
    avl.traverseInorder()

def run_delete_case():
    print (" ============= RUNNING DELETE CASE ================= ")
    avl = AVL()
    avl.insert(1)
    avl.insert(2)
    avl.insert(3)
    avl.insert(4)
    avl.insert(5)
    avl.traverseInorder()
    avl.removeData(1)

if __name__ == '__main__':
    run_left_heavy_case()
    run_right_heavy_case()
    run_left_right_case()
    run_right_left_case()
    run_delete_case()
