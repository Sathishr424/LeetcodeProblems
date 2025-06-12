# Last updated: 12/6/2025, 5:37:41 am
import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, can: int) -> int:
        n = len(costs)
        left, right = [], []  # Min-heaps
        left_index, right_index = 0, n - 1

        # Initialize left and right heaps
        if n >= can * 2:
            for _ in range(can):
                heapq.heappush(left, costs[left_index])
                heapq.heappush(right, costs[right_index])
                left_index += 1
                right_index -= 1
        else:
            for i in range(n):
                heapq.heappush(left, costs[i])
                left_index += 1

        ret = 0
        for _ in range(k):
            if left and right:
                if left[0] <= right[0]:  # Pick from left
                    ret += heapq.heappop(left)
                    if left_index <= right_index:
                        heapq.heappush(left, costs[left_index])
                        left_index += 1
                else:  # Pick from right
                    ret += heapq.heappop(right)
                    if right_index >= left_index:
                        heapq.heappush(right, costs[right_index])
                        right_index -= 1
            elif left:
                ret += heapq.heappop(left)
            elif right:
                ret += heapq.heappop(right)
            else:
                break  # No workers left

        return ret
