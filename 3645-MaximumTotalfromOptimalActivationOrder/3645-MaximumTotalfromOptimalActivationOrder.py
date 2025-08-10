# Last updated: 10/8/2025, 9:52:54 am
class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        n = len(value)
        new_arr = []

        for i in range(n):
            new_arr.append((limit[i], value[i], i))
        new_arr.sort(key=lambda x: (x[0], -x[1]))

        heap = []
        for i in range(n):
            heapq.heappush(heap, (limit[i], i))
        
        can_use = [1] * n
        active = 0
        ret = 0
        used = [0] * n

        for i in range(n):
            if can_use[new_arr[i][2]] and new_arr[i][0] > active:
                ret += new_arr[i][1]
                used[new_arr[i][2]] = 1
                active += 1
            
            old_active = active
            while heap and heap[0][0] <= old_active:
                _, index = heapq.heappop(heap)
                can_use[index] = 0
                if used[index]: active -= 1
        
        return ret
        