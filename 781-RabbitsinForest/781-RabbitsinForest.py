# Last updated: 20/4/2025, 1:02:56 pm
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        n = len(answers)
        ret = 0

        freq = defaultdict(int)

        for num in answers:
            freq[num] += 1

        for num in freq:
            if num == 0: ret += freq[num]
            elif freq[num] <= num+1: ret += num + 1
            else:
                x = freq[num] // (num+1)
                ret += x * (num+1)
                if freq[num] % (num+1): ret += num + 1
                
        return ret