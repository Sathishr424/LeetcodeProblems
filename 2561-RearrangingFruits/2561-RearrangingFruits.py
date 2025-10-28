# Last updated: 28/10/2025, 7:41:54 pm
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        n = len(basket1)

        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        both = set()
        for i in range(n):
            both.add(basket1[i])
            both.add(basket2[i])
            
            freq1[basket1[i]] += 1
            freq2[basket2[i]] += 1

        for num in both:
            if (freq1[num] + freq2[num]) % 2: return -1
            
        arr = []
        mini = inf
        for num in both:
            a = freq1[num]
            b = freq2[num]

            d = abs(a - b) // 2
            arr += [num] * d

            mini = min(num, mini)
        
        arr.sort()
        return sum([ min(mini * 2, num) for num in arr[:len(arr) // 2] ])