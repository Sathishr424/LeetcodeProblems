# Last updated: 12/6/2025, 5:49:05 am
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left = []
        right = []

        for i in range(k):
            heapq.heappush(left, -nums[i])
            heapq.heappush(right, -heapq.heappop(left))

            if len(right) > len(left):
                heapq.heappush(left, -heapq.heappop(right))
        
        ret = []
        if k % 2 == 0:
            ret.append((-left[0]+right[0]) / 2)
        else:
            ret.append(-left[0])

        deleted = defaultdict(int)

        for i in range(k, len(nums)):
            prev = nums[i-k]
            deleted[prev] += 1
            balance = 1

            if prev <= ret[-1]: balance = -1
            
            num = nums[i]

            if num <= ret[-1]:
                balance += 1
                heapq.heappush(left, -num)
            else:
                balance -= 1
                heapq.heappush(right, num)
            
            if balance < 0:
                heapq.heappush(left, -heapq.heappop(right))
            elif balance > 0:
                heapq.heappush(right, -heapq.heappop(left))
            
            while left and deleted[-left[0]] > 0:
                deleted[-left[0]] -= 1
                heapq.heappop(left)

            while right and deleted[right[0]] > 0:
                deleted[right[0]] -= 1
                heapq.heappop(right)

            if k % 2 == 0:
                ret.append((-left[0]+right[0]) / 2)
            else:
                ret.append(-left[0])
        
        return ret

