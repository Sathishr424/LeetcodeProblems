# Last updated: 18/4/2025, 8:36:33 pm
def getMaxK(nums, k, n):
    if k >= n: return nums
    stack = []
    
    for i, num in enumerate(nums):
        while stack and stack[-1] < num:
            if len(stack) + (n-i) == k: break
            stack.pop()
        
        stack.append(num)
    
    return stack[:k]

def greater(left, right, l, r):
    while l < len(left) and r < len(right) and left[l] == right[r]:
        l += 1
        r += 1
    
    return r == len(right) or (l < len(left) and left[l] > right[r])

def merge(left, right, compare):
    ret = []
    l = 0
    r = 0
    k = 0
    valid = False

    def check_valid():
        nonlocal valid
        if not valid: 
            if ret[k] < compare[k]: return False
            elif ret[k] > compare[k]: valid = True
        return True

    while l < len(left) and r < len(right):
        if greater(left, right, l, r):
            ret.append(left[l])
            l += 1
        else:
            ret.append(right[r])
            r += 1
        if not check_valid(): return compare
        k += 1
    
    while l < len(left):
        ret.append(left[l])
        if not check_valid(): return compare
        l += 1
        k += 1
    
    while r < len(right):
        ret.append(right[r])
        if not check_valid(): return compare
        r += 1
        k += 1
    
    return ret

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m = len(nums1)
        n = len(nums2)

        ret = [0] * k
        
        for l in range(max(0, k-n), min(m, k)+1):
            left = getMaxK(nums1, l, m)
            right = getMaxK(nums2, k-l, n)
            
            ret = merge(left, right, ret)
        
        return ret