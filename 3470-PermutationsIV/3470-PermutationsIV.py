# Last updated: 20/4/2025, 11:52:53 pm
@cache
def fact(x, y):
    if x == 0 or y == 0: return 1
    return x * fact(y, x-1)

class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        def perm(nums, k, is_odd):
            # print(nums, k, is_odd)
            n = len(nums)
            if n == 1: return nums
            odds = []
            evens = []
            for num in nums:
                if num % 2:
                    odds.append(num)
                else:
                    evens.append(num)
            if is_odd:
                for i, even in enumerate(evens):
                    f = fact(len(odds), len(evens)-1)
                    # print(even, k, f)
                    if f >= k:
                        rem = evens[:i] + evens[i+1:] + odds
                        return [even] + perm(rem, k, False)
                    k -= f
            else:
                for i, odd in enumerate(odds):
                    f = fact(len(evens), len(odds)-1)
                    # print(odd, k, f)
                    if f >= k:
                        rem = odds[:i] + odds[i+1:] + evens
                        return [odd] + perm(rem, k, True)
                    k -= f
            return []
        
        nums = [i for i in range(1, n+1)]

        odds = []
        evens = []
        for num in nums:
            if num % 2:
                odds.append(num)
            else:
                evens.append(num)
        # print(nums)
        if n % 2:
            for i, num in enumerate(odds):
                f = fact(len(evens), len(odds)-1)

                # print(num, k, f)
                if f >= k:
                    return [num] + perm(evens + odds[:i] + odds[i+1:], k, True)
                k -= f
        else:
            for i, num in enumerate(nums):
                if num % 2:
                    f = fact(len(evens), len(odds)-1)
                else:
                    f = fact(len(odds), len(evens)-1)
                # print(num, k, f)
                if f >= k:
                    return [num] + perm(nums[:i] + nums[i+1:], k, num % 2 == 1)
                k -= f
        return []