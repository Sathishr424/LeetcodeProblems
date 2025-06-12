# Last updated: 12/6/2025, 5:50:23 am
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = deque(nestedList)
        self.stack = deque([])
        self.populate()
    
    def populate(self):
        while not self.stack and self.list:
            self.populateStack(self.list.popleft())
    
    def populateStack(self, nes):
        if nes.isInteger():
            self.stack.append(nes.getInteger())
        else:
            for n in nes.getList():
                self.populateStack(n)
    
    def next(self) -> int:
        ans = self.stack.popleft()
        self.populate()
        return ans

    def hasNext(self) -> bool:
        return len(self.stack) > 0