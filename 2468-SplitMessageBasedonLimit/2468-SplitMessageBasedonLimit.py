# Last updated: 27/9/2025, 7:44:11 pm
class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        def canPart(part):
            cnt = 3 + len(str(part))
            rem = n
            parts = 0
            for i in range(0, 5):
                curr = 10 ** i
                if curr > part: break
                next = min(part, 10 ** (i + 1) - 1)
                elements = next - curr + 1
                new_length = cnt + (i + 1)
                rem -= (limit - new_length) * elements
                parts += elements
                if parts > part: return False
                if parts == part and next == part and rem > -(limit - new_length) and rem <= 0: return True
                if rem <= 0: return False
            
            return False

        def getTheString(part):
            m = len(str(part))
            ret = []
            index = 0
            for i in range(1, part + 1):
                cnt = 3 + m + len(str(i))
                need = limit - cnt
                curr = message[index:index+need]
                index += need
                ret.append(f"{curr}<{i}/{part}>")
            return ret
        
        for part in range(1, n + 1):
            if canPart(part):
                return getTheString(part)
        
        return []