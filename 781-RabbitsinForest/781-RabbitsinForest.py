# Last updated: 20/4/2025, 1:19:27 pm
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ret = 0
        freq = Counter(answers)

        for num in freq:
            cnt = freq[num]
            num += 1

            ret += ceil(cnt / num) * num
                
        return ret