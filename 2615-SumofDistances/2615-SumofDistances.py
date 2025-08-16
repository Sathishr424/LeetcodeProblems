# Last updated: 16/8/2025, 11:05:23 am
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)

        indexes = defaultdict(list)
        curr_index = defaultdict(int)
        for i in range(n):
            indexes[nums[i]].append(i)

        from_left = defaultdict(list)
        from_right = defaultdict(list)
        for num in indexes:
            curr_index[num] = 0
            curr = indexes[num]
            from_left[num] = [0] * len(curr)
            for i in range(1, len(curr)):
                prev = from_left[num][i - 1]
                diff = curr[i] - curr[i - 1]
                from_left[num][i] = diff * i + prev
            
            from_right[num] = [0] * len(curr)
            for i in range(len(curr)-2, -1, -1):
                prev = from_right[num][i + 1]
                diff = curr[i + 1] - curr[i]
                from_right[num][i] = diff * (len(curr) - i - 1) + prev

        ret = [0] * n
        for i in range(n):
            index = curr_index[nums[i]]
            ret[i] = from_left[nums[i]][index] + from_right[nums[i]][index]
            curr_index[nums[i]] += 1
        
        return ret
        