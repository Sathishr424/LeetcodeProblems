# Last updated: 17/6/2025, 8:50:06 am
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
        index = self.arr.bisect_left((endTime, 0))
        # print(index, curr)
        # print(self.arr)
        for i in range(min(index, len(self.arr) - 1), -1, -1):
            # if self.arr[i][1] <= startTime: break
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