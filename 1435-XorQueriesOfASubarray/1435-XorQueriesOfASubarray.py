# Last updated: 12/6/2025, 5:42:25 am
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = []
        p = 0

        for num in arr:
            p ^= num
            prefix.append(p)
        
        ret = []
        for i, j in queries:
            right = p ^ prefix[j]
            left = prefix[i] ^ arr[i]
            ret.append(p ^ left ^ right)
        return ret