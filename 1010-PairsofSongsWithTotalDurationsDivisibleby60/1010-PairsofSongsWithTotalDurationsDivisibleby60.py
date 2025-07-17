# Last updated: 17/7/2025, 7:05:04 pm
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n = len(time)

        counter = [0] * 60
        k = 60
        ret = 0

        for i in range(n):
            curr = time[i] % k
            need = (k - curr) % k

            ret += counter[need]

            counter[curr] += 1
    
        return ret