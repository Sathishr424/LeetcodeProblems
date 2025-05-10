# Last updated: 10/5/2025, 9:39:08 pm
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        freq = defaultdict(int)

        for num in nums:
            prev = -1
            while stack and stack[-1] > num:
                p = stack.pop()
                freq[p] += p != prev
                prev = p
            stack.append(num)

        prev = -1
        for num in stack:
            if num == prev or num == 0: continue
            freq[num] += 1
            prev = num

        return sum(freq.values())

            