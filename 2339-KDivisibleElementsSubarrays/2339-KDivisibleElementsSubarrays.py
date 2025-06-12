# Last updated: 12/6/2025, 5:38:23 am
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        m = 1000003
        mod = 10**9 + 7

        def rolling_hash_add(num, val):
            return ((num * m % mod) + val) % mod
        
        def rolling_hash_delete(num, val, distance):
            return (num - (val * pow(m, distance, mod) % mod)) % mod

        visited = {}
        for i in range(n):
            div = 0
            left = i
            num = 0
            for j in range(i, n):
                if nums[j] % p == 0: div += 1
                if div > k:
                    while left < j and div > k:
                        div -= nums[left] % p == 0
                        num = rolling_hash_delete(num, nums[left], j-left-1)
                        left += 1
                
                num = rolling_hash_add(num, nums[j])
                visited[num] = 1

        return len(visited)
