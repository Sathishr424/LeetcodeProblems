# Last updated: 9/4/2025, 10:23:39 pm
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ret = []

        l = 0
        r = 0

        # a
        # ab

        # aac
        # aab

        while l < len(word1) and r < len(word2):
            if word1[l] > word2[r]:
                ret.append(word1[l])
                l += 1
            elif word1[l] < word2[r]:
                ret.append(word2[r])
                r += 1
            else:
                if word1[l:] > word2[r:]:
                    ret.append(word1[l])
                    l += 1
                else:
                    ret.append(word2[r])
                    r += 1
            # print(word1[l:])
            # print(word2[r:])
            # print(''.join(ret))

            # print()
        while l < len(word1):
            ret.append(word1[l])
            l += 1
        
        while r < len(word2):
            ret.append(word2[r])
            r += 1
        
        return ''.join(ret)


