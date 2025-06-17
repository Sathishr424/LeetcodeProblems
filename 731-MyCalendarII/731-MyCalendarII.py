# Last updated: 17/6/2025, 8:57:45 am
class MyCalendarTwo:
    def __init__(self):
        self.arr = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        def collision(left, right):
            if left[0] > right[0]:
                left, right = right, left
            
            if right[0] >= left[0] and right[0] < left[1]:
                return True

            return False
        
        curr = (startTime, endTime)
        intersect = -1
        index = self.arr.bisect_left((endTime, 0))

        for i in range(min(index, len(self.arr) - 1), -1, -1):
            if collision(curr, self.arr[i]):
                if intersect != -1 and collision(self.arr[intersect], self.arr[i]):
                    return False
                intersect = i

        self.arr.add(curr)
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)