# Last updated: 12/25/2025, 7:11:04 PM
class Solution:
    def generateTag(self, caption: str) -> str:
        caption = caption.lower()
        ret = ['#']
        prev = False
        for char in caption:
            a = ord(char)
            if a >= ord('a') and a <= ord('z'):
                if prev:
                    ret.append(char.upper())
                else:
                    ret.append(char)
                prev = False
                if len(ret) == 100: return ''.join(ret) 
            elif char == ' ' and len(ret) > 1:
                prev = True

        return ''.join(ret)