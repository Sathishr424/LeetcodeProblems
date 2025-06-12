# Last updated: 12/6/2025, 5:46:11 am
class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.arr = [-1 for _ in range(k)]
        self.head = 0
        self.tail = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size < self.cap:
            self.tail += 1
            if self.tail == self.cap: self.tail = 0
            self.arr[self.tail] = value
            self.size += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.size >= 1:
            self.head += 1
            if self.head == self.cap: self.head = 0
            self.size -= 1
            return True
        return False

    def Front(self) -> int:
        return self.arr[self.head] if self.size > 0 else -1

    def Rear(self) -> int:
        return self.arr[self.tail] if self.size > 0 else -1
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()