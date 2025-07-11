# Last updated: 11/7/2025, 10:45:39 pm
class TextEditor:
    def __init__(self):
        self.left = deque([])
        self.right = deque([])

    def addText(self, text: str) -> None:
        for char in text:
            self.left.append(char)
        # print(self.left, self.right)

    def deleteText(self, k: int) -> int:
        i = 0
        while len(self.left) and i < k:
            self.left.pop()
            i += 1
        # print(self.left, self.right)
        return i

    def cursorLeft(self, k: int) -> str:
        i = 0
        while i < k and len(self.left):
            self.right.appendleft(self.left.pop())
            i += 1
        
        # print(self.left, self.right)
        ret = ''
        m = max(0, len(self.left) - 10)
        for i in range(m, len(self.left)):
            ret += self.left[i]
        return ret

    def cursorRight(self, k: int) -> str:
        i = 0
        while i < k and len(self.right):
            self.left.append(self.right.popleft())
            i += 1
        
        # print(self.left, self.right)
        ret = ''
        m = max(0, len(self.left) - 10)
        for i in range(m, len(self.left)):
            ret += self.left[i]
        return ret

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)