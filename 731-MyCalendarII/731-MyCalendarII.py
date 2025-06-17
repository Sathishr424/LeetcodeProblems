# Last updated: 17/6/2025, 8:27:22 am
class MyCalendarTwo:
    def __init__(self):
        self.arr = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        # (1, 5) (4, 8)
        # (4, 8) (5, 7)
        def collision(left, right):
            res = False
            if left[0] > right[0]:
                left, right = right, left
            
            if right[0] >= left[0] and right[0] < left[1]:
                res = True
            # print(left, right, res)
            return res
        
        intersect = -1
        res = True
        for i, (x, y) in enumerate(self.arr):
            if collision(self.arr[i], (startTime, endTime)):
                if intersect != -1 and collision(self.arr[intersect], self.arr[i]):
                    res = False
                    break
                intersect = i
        # print(self.arr)
        # print((startTime, endTime), res, '====>')
        if res:
            self.arr.add((startTime, endTime))
        return res


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)