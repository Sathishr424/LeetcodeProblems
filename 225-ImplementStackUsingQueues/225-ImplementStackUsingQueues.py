# Last updated: 12/6/2025, 5:51:27 am
class MyStack:
    def __init__(self):
        self.s1 = deque([])
        self.topElement = None

    def push(self, x: int) -> None:
        self.s1.append(x)
        self.topElement = x

    def pop(self) -> int:
        s2 = deque([])
        tmp = None
        while len(self.s1) > 1:
            tmp = self.s1.popleft()
            s2.append(tmp)
        self.topElement = tmp
        tmp = self.s1.popleft()
        self.s1 = s2
        return tmp

    def top(self) -> int:
        return self.topElement

    def empty(self) -> bool:
        return len(self.s1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()