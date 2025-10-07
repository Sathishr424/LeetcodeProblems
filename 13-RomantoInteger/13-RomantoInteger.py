# Last updated: 7/10/2025, 11:09:42 am
class Solution:
    def romanToInt(self, roman: str) -> int:
        n = len(roman)
        
        relation = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        relation_index = {
            'I': 1,
            'V': 2,
            'X': 3,
            'L': 4,
            'C': 5,
            'D': 6,
            'M': 7,
        }
        
        # IV, VI
        
        ans = 0
        i = 0
        while i < n:
            index = relation_index[roman[i]]
            if i + 1 < n and relation_index[roman[i + 1]] == index + 1:
                ans += relation[roman[i + 1]] - relation[roman[i]]
                i += 1
            elif i + 1 < n and relation_index[roman[i + 1]] == index + 2:
                ans += relation[roman[i + 1]] - relation[roman[i]]
                i += 1
            else:
                ans += relation[roman[i]]
            i += 1
        
        return ans
        