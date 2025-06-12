# Last updated: 12/6/2025, 5:36:26 am
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        possible1 = []
        possible1.append(f"{s1[2]}{s1[1]}{s1[0]}{s1[3]}")
        possible1.append(f"{s1[2]}{s1[3]}{s1[0]}{s1[1]}")
        possible1.append(f"{s1[0]}{s1[3]}{s1[2]}{s1[1]}")

        possible2 = []
        possible2.append(f"{s2[2]}{s2[1]}{s2[0]}{s2[3]}")
        possible2.append(f"{s2[2]}{s2[3]}{s2[0]}{s2[1]}")
        possible2.append(f"{s2[0]}{s2[3]}{s2[2]}{s2[1]}")

        for i in range(3):
            for j in range(3):
                if possible1[i] == possible2[j]: return True
        return False
        