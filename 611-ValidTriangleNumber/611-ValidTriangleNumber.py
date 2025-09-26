# Last updated: 26/9/2025, 2:03:36 pm
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        queries = []
        for i in range(n):
            for j in range(i+1, n):
                a = nums[i]
                b = nums[j]

                left = abs(a - b) + 1
                right = a + b - 1

                if left <= right:
                    queries.append((j+1, left, right))

        queries.sort()
        sl = SortedList()
        index = n - 1
        for i in range(len(queries)-1, -1, -1):
            j, left, right = queries[i]
            while index >= j:
                sl.add(nums[index])
                index -= 1
            l = sl.bisect_left(left)
            r = sl.bisect_right(right)
            cnt += r - l

        return cnt