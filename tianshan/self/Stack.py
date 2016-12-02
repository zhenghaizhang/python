class Stack():
    def __init__(self, size):
        self.stack = [];
        self.size = size;
        self.top = 0;

    def push(self, content):
        if self.full():
            print("Stack is Full!")
        else:
            self.stack.append(content)
            self.top += 1

    def full(self):
        if self.top == self.size:
            return True;
        else :
            return False;

    def empty(self ):
        if self.top == 0:
            return True;
        else :
            return False;

    def out(self):
        if self.empty():
            print("Stack is Empty!")
        else:
            self.top -= 1

q = Stack(1)
print(q.empty())
print(q.full())