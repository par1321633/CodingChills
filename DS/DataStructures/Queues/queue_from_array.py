

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

if __name__ == '__main__':
    print ("Initiating Queue")
    q = Queue()
    print ("Adding 10 to queue")
    q.enqueue(10)
    print ("Adding 12 to queue")
    q.enqueue(12)
    print ("Adding at queue")
    q.peek()
    print ("Pushing 11 to queue")
    q.enqueue(11)
    print ("Peeking at queue")
    q.peek()
    print ("Removing from queue")
    q.dequeue()
    print ("Removing from queue")
    q.dequeue()
    print ("Checking if queue is empty")
    q.is_empty()
    print ("Removing from queue")
    q.dequeue()
    print ("Checking if queue is empty")
    q.is_empty()
    print ("Removing from queue")
    q.dequeue()
