# Last updated: 23/5/2025, 10:53:50 am
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]], second=0) -> int:
        n = len(nums)
        
        heap = []
        for num in nums:
            heapq.heappush(heap, (-((num ^ k) - num), num ^ k, num))
        # print(heap)
        ret = 0
        later = []
        another = []
        while heap:
            while heap and heap[0][1] < heap[0][2]:
                later.append(heapq.heappop(heap)[1:])
            if not heap: break

            x = heapq.heappop(heap)
            while heap and heap[0][1] < heap[0][2]:
                later.append(heapq.heappop(heap)[1:])
            
            if not heap:
                another.append(x[1:])
                break
            
            y = heapq.heappop(heap)
            ret += x[1]
            ret += y[1]
        
        later.sort(key=lambda x: x[1] - x[0])
        
        # print(ret)
        for xnum, num in later:
            ret += num
        
        # print(later)
        # print(another)
        new_ret = ret
        if another:
            ret += another[0][1]
            if later:
                new_ret -= later[0][1]
                new_ret += later[0][0]

                new_ret += another[0][0]
            else:
                new_ret += another[0][1]


        return max(ret, new_ret)