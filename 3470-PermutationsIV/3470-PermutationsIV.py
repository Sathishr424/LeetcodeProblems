# Last updated: 21/4/2025, 12:22:28 am
@cache
def fact(x, y):
    if x == 0 or y == 0: return 1
    return x * fact(y, x-1)

class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        def perm(evens, odds, k):
            for i, num in enumerate(evens):
                f = fact(len(odds), len(evens)-1)
                if f >= k:
                    return [num] + perm(odds, evens[:i] + evens[i+1:], k)
                k -= f
            return []
        
        odds = []
        evens = []
        nums = []
        for i in range(1, n+1):
            nums.append(i)
            if i % 2: odds.append(i)
            else: evens.append(i)
        if n % 2:
            return perm(odds, evens, k)
        else:
            for i, num in enumerate(nums):
                if num % 2:
                    f = fact(len(evens), len(odds)-1)
                    if f >= k:
                        i = i // 2
                        return [num] + perm(evens, odds[:i] + odds[i+1:], k)
                else:
                    f = fact(len(odds), len(evens)-1)
                    if f >= k:
                        i = i // 2
                        return [num] + perm(odds, evens[:i] + evens[i+1:], k)
                k -= f
        
        return []