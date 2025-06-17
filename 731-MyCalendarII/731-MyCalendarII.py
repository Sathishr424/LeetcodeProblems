# Last updated: 17/6/2025, 8:39:50 am
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
        
        curr = (startTime, endTime)
        intersect = -1
        res = True
        left = self.arr.bisect_left((0, endTime))
        # right = self.arr.bisect_right((0, endTime))
        # right = len(self.arr)
        # print((left, right))
        for i in range(left, len(self.arr)):
            if collision(self.arr[i], curr):
                if intersect != -1 and collision(self.arr[intersect], self.arr[i]):
                    res = False
                    break
                intersect = i
        
        # print(self.arr)
        # print((startTime, endTime), res, '====>')

        if res:
            self.arr.add(curr)
        return res


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)