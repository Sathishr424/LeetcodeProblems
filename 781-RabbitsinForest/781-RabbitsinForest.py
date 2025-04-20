# Last updated: 20/4/2025, 1:06:39 pm
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ret = 0

        freq = defaultdict(int)

        for num in answers:
            freq[num+1] += 1

        for num in freq:
            cnt = freq[num]

            ret += cnt // num * num
            if cnt % num: ret += num
                
        return ret