# Last updated: 15/10/2025, 12:29:03 am
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if s == target: return True
        n = len(s)
        convert_to_one = 0
        convert_to_zero = 0
        spare_one = 0
        for i in range(n):
            if s[i] != target[i]:
                if target[i] == '1':
                    convert_to_one += 1
                else:
                    convert_to_zero += 1
            elif s[i] == '1':
                spare_one += 1
        # print(convert_to_one)
        # print(convert_to_zero)
        # print(spare_one)
        if convert_to_one and spare_one + convert_to_zero == 0: return False
        if convert_to_one == 0 and spare_one == 0: return False
        return True