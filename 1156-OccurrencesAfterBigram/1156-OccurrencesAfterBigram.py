# Last updated: 12/6/2025, 5:43:52 am
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split(' ')
        if len(text) < 3: return []

        ret = []
        for i in range(len(text)-2):
            if text[i] == first and text[i+1] == second:
                ret.append(text[i+2])
        
        return ret