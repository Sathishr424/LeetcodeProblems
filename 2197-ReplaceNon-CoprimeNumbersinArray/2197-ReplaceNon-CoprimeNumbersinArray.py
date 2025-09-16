# Last updated: 16/9/2025, 6:45:37 am
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        for num in nums:
            stack.append(num)
            while len(stack) > 1 and gcd(stack[-2], stack[-1]) > 1:
                y = stack.pop()
                stack[-1] = lcm(stack[-1], y)
        
        return stack