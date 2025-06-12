# Last updated: 12/6/2025, 5:38:55 am
class Solution:
    def minimizedMaximum(self, n: int, q: List[int]) -> int:
        l = 1
        q.sort(reverse=True)
        r = max(q)
        ans = r
        while l <= r:
            mid = (l+r)//2
            rem = n
            res = 0
            for quan in q:
                t = ceil(quan/mid)
                rem -= t
                if rem < 0:
                    l = mid+1
                    break
                res = max(res, mid)
            
            if rem >= 0:
                r = mid-1
                ans = min(ans, res)
        return ans
