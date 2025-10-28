# Last updated: 28/10/2025, 8:43:31 pm
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n = len(s)

        values = {}
        for i in range(n):
            if s[i] == '0':
                values[0] = i
                break
        
        for bit in range(1, min(32, n + 1)):
            curr = 0
            val = 1 << (bit - 1)
            for i in range(bit):
                b = int(s[i])
                curr += b * pow(2, bit - i - 1)
            
            if s[0] != '0' and (curr not in values or values[curr] > 0):
                values[curr] = 0

            for i in range(bit, n):
                if s[i - bit] == '1':
                    curr -= val
                curr *= 2
                b = int(s[i])
                curr += b

                index = i - bit + 1
                if s[i-bit+1] != '0' and (curr not in values or values[curr] > index):
                    values[curr] = index

                # print(bit, curr, (i-bit+1, i), s[i-bit+1:i+1])

        # print(values)
        ret = []
        for s, e in queries:
            need = s ^ e
            if need in values:
                left = values[need]
                if need == 0:
                    ret.append([left, left])
                else:
                    ret.append([left, left + need.bit_length() - 1])
            else:
                ret.append([-1, -1])
        
        return ret