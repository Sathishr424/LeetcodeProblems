# Last updated: 1/7/2025, 7:15:38 am
class Solution:
    def stringSequence(self, target: str) -> List[str]:
        n = len(target)

        curr = ''
        index = 0
        ret = []
        while curr != target:
            for i in range(ord(target[index]) - 97 + 1):
                ret.append(curr + chr(i + 97))
            index += 1
            curr = ret[-1]
        
        return ret