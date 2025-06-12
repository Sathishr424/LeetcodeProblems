# Last updated: 12/6/2025, 5:47:19 am
class MyCalendar:
    def __init__(self):
        self.arr = SortedList()
    
    def bn(self, start, end):
        l = 0
        r = len(self.arr)

        while l < r:
            mid = (l+r) // 2

            if self.arr[mid][0] >= start:
                r = mid
            else:
                l = mid+1
        
        if l < len(self.arr):
            if self.arr[l][0] < end: return False

        if l-1 >= 0:
            if self.arr[l-1][1] > start: return False

        return True

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.bn(startTime, endTime): return False
        self.arr.add((startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)