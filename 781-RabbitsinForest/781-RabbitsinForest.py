# Last updated: 20/4/2025, 1:14:20 pm
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        prev = answers[0]
        cnt = 1
        ret = 0
        
        def calc(num, cnt):
            return cnt // num * num + (num if cnt % num else 0)

        for i in range(1, len(answers)):
            num = answers[i]
            if num == prev:
                cnt += 1
            else:
                ret += calc(prev+1, cnt)
                cnt = 1
            prev = num
                
        return ret + calc(prev+1, cnt)