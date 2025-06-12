# Last updated: 12/6/2025, 5:42:05 am
class ProductOfNumbers:

    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        if num > 0:
            if len(self.nums) > 0:
                self.nums.append(self.nums[-1] * num)
            else:
                self.nums.append(num)
        else:
            self.nums = []
        
        
    def getProduct(self, k: int) -> int:
        n = len(self.nums)

        if k > n: return 0
        j = n - k

        if j == 0: return self.nums[-1]
        else: return self.nums[-1] // self.nums[j-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)