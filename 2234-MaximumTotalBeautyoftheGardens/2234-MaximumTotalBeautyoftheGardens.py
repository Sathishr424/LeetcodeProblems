# Last updated: 9/9/2025, 1:08:53 am
class Solution:
    def maximumBeauty(self, flowers: List[int], k: int, target: int, full: int, partial: int) -> int:
        n = len(flowers)
        flowers.sort()

        right = bisect_left(flowers, target)
        complete = n - right

        prefix = [0] * (n + 1)
        need = 0
        for i in range(n-1, -1, -1):
            need += max(0, target - flowers[i])
            prefix[i] = need
        
        partial_prefix = [0] * n
        cnt = 0
        for i in range(1, n):
            diff = flowers[i] - flowers[i - 1]
            cnt += diff * i
            partial_prefix[i] = cnt
        
        # print(flowers)
        # print(prefix)
        # print(partial_prefix)

        def isGood(mid, rem, c):
            index = bisect_left(flowers, mid, hi=n-c) - 1
            if index < 0: return True

            cnt = partial_prefix[index]
            diff = mid - flowers[index]

            return cnt + (index + 1) * diff <= rem

        max_ans = -1
        for c in range(complete, n + 1):
            need = prefix[n-c]
            if need > k: break

            rem = k - need

            l = 0
            r = target - 1
            if c < n: 
                while l < r:
                    mid = (l + r + 1) // 2
                    
                    if isGood(mid, rem, c):
                        l = mid
                    else:
                        r = mid - 1
            
            curr = c * full + l * partial
            max_ans = max(max_ans, curr)

        return max_ans