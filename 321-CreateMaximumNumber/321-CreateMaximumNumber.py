# Last updated: 18/4/2025, 7:54:17 pm
def getMinK(nums, k, n):
    if k >= n: return nums
    stack = []
    
    for i, num in enumerate(nums):
        while stack and stack[-1] < num:
            if len(stack) + (n-i) == k: break
            stack.pop()
        
        stack.append(num)
    
    return stack[:k]

def merge(left, right):
    ret = []
    s1 = ''.join([str(i) for i in left])
    s2 = ''.join([str(i) for i in right])
    
    l = 0
    r = 0
    while s1 and s2:
        if s1 > s2:
            ret.append(left[l])
            s1 = s1[1:]
            l += 1
        else:
            ret.append(right[r])
            s2 = s2[1:]
            r += 1
    
    while l < len(left):
        ret.append(left[l])
        l += 1
    while r < len(right):
        ret.append(right[r])
        r += 1
    
    return ret

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m = len(nums1)
        n = len(nums2)

        ret = [0] * k
        
        for l in range(max(0, k-n), min(m, k)+1):
            left = getMinK(nums1, l, m)
            right = getMinK(nums2, k-l, n)
            
            res = merge(left, right)
            for i in range(k):
                if res[i] == ret[i]: continue
                elif res[i] > ret[i]: ret = res
                break
                    
        return ret



