# Last updated: 12/6/2025, 5:42:44 am
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        n = len(nums)

        # Count occurrences of each product
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1

        # Calculate the result
        result = 0
        for count in product_count.values():
            if count > 1:
                result += (count * (count - 1) // 2) * 8  # Use direct formula

        return result
