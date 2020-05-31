class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            print ("No ROOT is there, Adding data as root")
            self.root = Node(data)
        else:
            self.insertNode(self.root, data)

    def insertNode(self, node, data):
        if node.data > data:
            print ("Node is greater than data : {} > {}".format(node.data, data))
            if node.leftChild:
                print ("Left Node Exist, Recursion Call")
                self.insertNode(node.leftChild, data)
            else:
                print ("Adding New Node")
                node.leftChild = Node(data)
        else:
            print ("Node is smaller than data : {} < {}".format(node.data, data))
            if node.rightChild:
                print ("Right Node Exist, Recursion Call")
                self.insertNode(node.rightChild, data)
            else:
                print ("Adding New Node")
                node.rightChild = Node(data)

    def getMin(self):
        curr = self.root
        if curr is None:
            print ("Tree is empty")
            return None
        while curr:
            if curr.leftChild:
                print ("Left Child Exist, Proceeding Further")
                curr = curr.leftChild
            else:
                return curr.data

    def getMinRecursion(self):
        if self.root:
            return self.getMinRec(self.root)
        else:
            print ("Tree is empty")
            return None

    def getMinRec(self, node):
        if node.leftChild:
            return self.getMinRec(node.leftChild)
        return node.data

    def getMax(self):
        curr = self.root
        if curr is None:
            print ("Tree is empty")
            return None
        while curr:
            if curr.rightChild:
                print ("Right Child Exist, Proceeding Further")
                curr = curr.rightChild
            else:
                return curr.data

    def getMaxRecursion(self):
        if self.root:
            return self.getMaxRec(self.root)
        else:
            print ("Tree is empty")
            return None

    def getMaxRec(self, node):
        if node.rightChild:
            return self.getMinRec(node.rightChild)
        return node.data

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


if __name__ == '__main__':
    print ("Creating BST Tree Obj")
    bst = BinarySearchTree()
    print ("Inserting Node 10 to tree")
    bst.insert(10)
    print ("Inserting Node 5 to tree")
    bst.insert(5)
    print ("Inserting Node 15 to tree")
    bst.insert(15)
    print ("Inserting Node 7 to tree")
    bst.insert(7)
    print ("Minimum Node of Tree is ")
    bst.getMin()
    bst.getMinRecursion()
    print ("Maximum Node of Tree is ")
    bst.getMax()
    bst.getMaxRecursion()
    print ("In order Traversal of Tree")
    bst.traverseInorder()




