# Last updated: 19/7/2025, 1:33:15 pm
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        n = len(folder)
        folder.sort(key=lambda x: len(x))

        ret = []
        starts = {}

        for i in range(n):
            is_sub = False
            for j in range(1, len(folder[i])):
                if folder[i][j] == '/':
                    if folder[i][:j] in starts:
                        is_sub = True
                        break
            if not is_sub:
                ret.append(folder[i])
                starts[folder[i]] = 1
        
        return ret