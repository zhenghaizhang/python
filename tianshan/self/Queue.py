class Queue():
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.head = -1
        self.tail = -1

    def empty(self):
        if self.head == self.tail:
            return True;
        else :
            return False

    def full(self):
        if self.tail - self.head == self.size:
            return True
        else:
            return False;

    def enQueue(self, content):
        if self.full():
            print("Queue is Full!")
        else:
            self.queue.append(content)
            self.tail += 1

    def outQueue(self):
        if self.empty():
            print("Queue is Empty!")
        else:
            self.queue.remove();
            self.head += 1

queue = Queue(1)
print(queue.empty())
queue.enQueue(1)
print(queue.full())