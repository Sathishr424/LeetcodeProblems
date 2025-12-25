# Last updated: 12/25/2025, 7:07:57 PM
def mergeSort(nums):
    if len(nums) <= 1:
        return 0
    
    half = len(nums) // 2
    left = nums[:half]
    right = nums[half:]
    
    ans = 0
    ans += mergeSort(left)
    ans += mergeSort(right)
    
    l = r = k = 0
    cnt = 0
    
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            nums[k] = left[l]
            l += 1
            ans += cnt
        else:
            nums[k] = right[r]
            r += 1
            cnt += 1
        k += 1
    
    while l < len(left):
        nums[k] = left[l]
        l += 1
        k += 1
        ans += cnt
    
    while r < len(right):
        nums[k] = right[r]
        r += 1
        k += 1

    return ans

class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        n = len(nums)

        cnt = 0
        sl = SortedList()
        for i in range(k):
            sl.add(nums[i])
            cnt += len(sl) - sl.bisect_right(nums[i])
        
        ans = cnt
        for i in range(k, n):
            prev = nums[i - k]
            cnt -= sl.bisect_left(prev)
            sl.remove(prev)

            sl.add(nums[i])
            cnt += len(sl) - sl.bisect_right(nums[i])
            ans = min(ans, cnt)

        return ans