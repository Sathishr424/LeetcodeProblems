# Last updated: 12/6/2025, 5:45:16 am
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(typed)
        m = len(name)

        if m > n: return False

        index = 0
        prev = None
        for w in typed:
            if index == m or w != name[index]:
                if w != prev: return False
            else:
                prev = w
                index += 1
        return index == m
