class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self,root):
        self.root = root

    def printInorder(self, root):
    # LEFT, ROOT, RIGHT
        if root:
            # First recur on left child
            self.printInorder(root.left)
            # then print the data of node
            print(root.val),
            # now recur on right child
            self.printInorder(root.right)

    def printInorderTraversal(self):
        self.printInorder(self.root)

    def printPostOrderTraversal(self):
        self.printPostorder(self.root)

    def printPostorder(self, root):
        if root:
            self.printPostorder(root.left)
            self.printPostorder(root.right)
            print (root.val)

    def printPreOrderTraversal(self):
        self.printPreorder(self.root)

    def printPreorder(self, root):
        if root:
            print(root.val)
            self.printPreorder(root.left)
            self.printPreorder(root.right)

    def printInorderUsingStacks(self):
        current = self.root
        stack = []
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif (stack):
                current = stack.pop()
                print (current.val)
                current = current.right
            else:
                break

    def printPreorderUsingStacks(self):
        current = self.root
        stack = []
        while True:
            if current:
                stack.append(current)
                print (current.val)
                current = current.left
            elif (stack):
                current = stack.pop()

                current = current.right
            else:
                break

    def printPostorderUsingStacks(self):
        current = self.root
        stack = []
        while True:
            if current:
                if current.right:
                    stack.append(current.right)
                stack.append(current)
                current = current.left
            elif (stack):
                current = stack.pop()
                print(current.val)
                current = current.right
            else:
                break