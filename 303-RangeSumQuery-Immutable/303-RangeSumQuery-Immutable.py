# Last updated: 8/7/2025, 6:49:02 pm
class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        k = floor(log2(n)) + 1
        self.s_table = [[0] * n for _ in range(k)]

        for i in range(n):
            self.s_table[0][i] = nums[i]
        
        for power in range(1, k):
            m = 1 << power
            prev_m = m >> 1
            for i in range(n - m + 1):
                self.s_table[power][i] = self.s_table[power - 1][i] + self.s_table[power - 1][i + prev_m]

    def sumRange(self, left: int, right: int) -> int:
        dis = right - left + 1
        power = 0
        ret = 0
        while dis:
            if dis & 1:
                ret += self.s_table[power][left]
                left += 1 << power
            dis >>= 1
            power += 1
        
        return ret


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)