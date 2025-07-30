# Last updated: 30/7/2025, 9:17:27 pm
from math import sqrt, ceil, floor
from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(nums)
        self.blockSize = int(sqrt(n)) + 1
        self.blocks = [0] * ((n + self.blockSize - 1) // self.blockSize)
        
        for i in range(n):
            self.blocks[i // self.blockSize] += nums[i]

    def update(self, index: int, val: int) -> None:
        block = index // self.blockSize
        self.blocks[block] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        s = 0
        while left <= right:
            if left % self.blockSize == 0 and left + self.blockSize - 1 <= right:
                s += self.blocks[left // self.blockSize]
                left += self.blockSize
            else:
                s += self.nums[left]
                left += 1
        return s