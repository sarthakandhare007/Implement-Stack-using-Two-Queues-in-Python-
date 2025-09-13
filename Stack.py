from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)
        
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1:
            raise Exception("Stack is empty")
        return self.q1.popleft()

    def top(self):
        if not self.q1:
            raise Exception("Stack is empty")
        return self.q1[0]

    def empty(self):
        return not self.q1

# Testing the stack
stack = StackUsingQueues()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.top())  # 30
print("Popped:", stack.pop())      # 30
print("Top element:", stack.top())  # 20
print("Empty?", stack.empty())     # False
