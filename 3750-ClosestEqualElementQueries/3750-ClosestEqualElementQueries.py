# Last updated: 12/6/2025, 5:34:45 am
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        exists = {}
        ret = []
        
        for i in queries:
            exists[nums[i]] = 1

        dis = defaultdict(list)

        for i in range(n):
            if nums[i] in exists:
                dis[nums[i]].append(i)
                    
        def bs(index, arr):
            l = 0
            r = len(arr)-1
            ans = n
            
            if arr[-1] != index:
                ans = min(ans, n - abs(arr[-1] - index))
                
            if index != arr[0]:
                ans = min(ans, n - abs(arr[0] - index))
            
            while l <= r:
                mid = (l+r)//2

                if arr[mid] < index:
                    l = mid+1
                elif arr[mid] > index:
                    r = mid-1
                else:
                    if mid+1 < len(arr):
                        ans = min(ans, arr[mid+1] - index, n - abs(arr[mid+1] - index))
                    if mid-1 >= 0:
                        ans = min( index - arr[mid-1], ans, n - abs(arr[mid-1] - index))

                    return ans
                    

        for i in queries:
            if len(dis[nums[i]]) > 1:
                ret.append(bs(i, dis[nums[i]]))
            else:
                ret.append(-1)

        return ret
            