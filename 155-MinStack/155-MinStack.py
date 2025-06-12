# Last updated: 12/6/2025, 5:52:14 am
class MinStack:
    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(( val, min(val, self.arr[-1][1] if self.arr else val) ))

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()