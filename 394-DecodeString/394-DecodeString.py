# Last updated: 12/6/2025, 5:49:54 am
class Solution:
    def decodeString(self, s: str) -> str:
        def helper(index):
            ret = ''
            i = index
            while i < len(s):
                if s[i] == ']': return [i, ret]
                elif s[i].isdigit():
                    curr = int(s[i])
                    start = i+1
                    while s[start] != '[':
                        curr = curr * 10 + int(s[start])
                        start += 1
                    end, st = helper(start+1)
                    ret += st * curr
                    i = end
                else:
                    ret += s[i]
                i += 1
            return ret
        return helper(0)

                    
                