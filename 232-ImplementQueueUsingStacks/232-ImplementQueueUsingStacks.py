# Last updated: 12/6/2025, 5:51:14 am
class MyQueue:

    def __init__(self):
        self.a1 = []
        self.a2 = []

    def push(self, x: int) -> None:
        self.a1.append(x)

    def pop(self) -> int:
        tmp = []
        while self.a1:
            tmp.append(self.a1.pop())
        self.a2 = tmp + self.a2
        return self.a2.pop()
        
    def peek(self) -> int:
        return self.a2[-1] if self.a2 else self.a1[0]

    def empty(self) -> bool:
        return not (self.a1 or self.a2)
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()