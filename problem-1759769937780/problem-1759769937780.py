# Last updated: 6/10/2025, 10:28:57 pm
class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.nums = []
        self.left = 0
        self.cnt = 0

    def consec(self, num: int) -> bool:
        self.nums.append(num)
        if num == self.value:
            self.cnt += 1
        if len(self.nums) - self.left > self.k:
            if self.nums[self.left] == self.value:
                self.cnt -= 1
            self.left += 1

        return self.cnt == self.k

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)