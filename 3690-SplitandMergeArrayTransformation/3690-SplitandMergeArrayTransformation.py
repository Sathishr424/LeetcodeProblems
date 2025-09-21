# Last updated: 21/9/2025, 9:56:21 am
class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums1 = [str(i) for i in nums1]
        nums2 = [str(i) for i in nums2]
        
        cnt = 0
        stack = [(nums1)]
        cached = {}
        cached[','.join(nums1)] = 1

        while stack:
            new_stack = []
            # if cnt == 1: print(stack)

            for nums in stack:
                if nums == nums2:
                    # print(nums, nums2)
                    return cnt
                for window in range(1, n):
                    for i in range(n-window+1):
                        sub_arr = nums[i:i+window]
                        rem = nums[:i] + nums[i+window:]
                        # if cnt <= 2: print(sub_arr, nums)
                        for j in range(len(rem) + 1):
                            new_nums = rem[:j] + sub_arr + rem[j:]
                            st = ','.join(new_nums)
                            if st not in cached:
                                new_stack.append(new_nums)
                                cached[st] = 1
            stack = new_stack
            cnt += 1
        
        return -1