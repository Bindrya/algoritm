from collections import deque

class MyStack:
    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int):
        self.queue_in.append(x)

    def pop(self) -> int:
        while len(self.queue_in) > 1:
            self.queue_out.append(self.queue_in.popleft())
        top = self.queue_in.popleft()
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return top

    def top(self) -> int:
        while len(self.queue_in) > 1:
            self.queue_out.append(self.queue_in.popleft())
        top = self.queue_in[0]
        self.queue_out.append(self.queue_in.popleft())
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return top

    def empty(self) -> bool:
        return len(self.queue_in) == 0

# Example usage
myStack = MyStack()
print(myStack.push(1)) 
print(myStack.push(2))  
print(myStack.top())    
print(myStack.pop())   
print(myStack.empty())  
