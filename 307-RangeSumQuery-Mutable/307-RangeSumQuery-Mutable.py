# Last updated: 30/7/2025, 9:17:53 pm
class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.n = n
        self.nums = nums

        self.blockSize = floor(sqrt(n)) + 1
        self.blocks = [0] * ceil(n / self.blockSize)

        s = 0
        index = 0
        for i in range(n):
            s += nums[i]
            if (i + 1) % self.blockSize == 0:
                self.blocks[index] = s
                index += 1
                s = 0
        
        if n % self.blockSize:
            self.blocks[index] = s

    def update(self, index: int, val: int) -> None:
        prev = self.nums[index]
        self.nums[index] = val
        block = index // self.blockSize
        self.blocks[block] -= prev - val

    def sumRange(self, left: int, right: int) -> int:
        s = 0

        l = ceil(left / self.blockSize)
        r = (right + 1) // self.blockSize - 1
        
        for i in range(l, r + 1):
            s += self.blocks[i]
        
        last = left
        for i in range(left, min(right + 1, l * self.blockSize)):
            s += self.nums[i]
            last = i + 1

        for i in range(max(last, (r + 1) * self.blockSize), right + 1):
            s += self.nums[i]
        
        return s
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)