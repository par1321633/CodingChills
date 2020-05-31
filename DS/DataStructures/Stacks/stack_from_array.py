

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def stack_size(self):
        return len(self.stack)


if __name__ == '__main__':
    print ("Initiating Stack")
    s = Stack()
    print ("Pushing 10 to stack")
    s.push(10)
    print ("Pushing 12 to stack")
    s.push(12)
    print ("Peeking at Stack")
    s.peek()
    print ("Pushing 11 to stack")
    s.push(11)
    print ("Peeking at Stack")
    s.peek()
    print ("Pop from stack")
    s.pop()
    print ("Pop from stack")
    s.pop()
    print ("Checking if stack is empty")
    s.is_empty()
    print ("Pop from stack")
    s.pop()
    print ("Checking if stack is empty")
    s.is_empty()
    print ("Pop from stack")
    s.pop()