# Last updated: 7/4/2025, 11:15:10 pm
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        tot = sum(nums)
        part = tot // k

        if tot / k != part: return False

        used = defaultdict(int)

        for num in nums:
            used[num] += 1

        dict_arr = sorted(used.keys())
        # print(dict_arr, tot, part)
        n = len(dict_arr)

        def rec(index, tot, parts, arr):
            nonlocal used
            if index == len(arr): return False

            for i in range(index, len(arr)):
                if arr[i]+tot <= part:
                    if used[arr[i]] == 0: continue
                    used[arr[i]] -= 1
                    if arr[i]+tot == part:
                        if parts+1 == k: return True
            
                        new_arr = []
                        for num in arr:
                            if used[num] > 0:
                                new_arr.append(num)
                        if rec(0, 0, parts+1, new_arr): return True
                    else:

                        if rec(i+(used[arr[i]] == 0), tot+arr[i], parts, arr): return True
                    used[arr[i]] += 1
                else: return False
            
            return False
            

        return rec(0, 0, 0, dict_arr)


