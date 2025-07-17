# Last updated: 17/7/2025, 8:11:24 pm
class Solution:
    def numberOfWeakCharacters(self, prop: List[List[int]]) -> int:
        n = len(prop)
        prop.sort(key=lambda x: -x[0])

        sl = SortedList()
        ret = 0
        # print(prop)
        i = 0
        while i < n:
            cnt = len(sl) - sl.bisect_right(prop[i][1])
            if cnt: ret += 1

            j = i + 1
            while j < n and prop[j][0] == prop[j-1][0]:
                cnt = len(sl) - sl.bisect_right(prop[j][1])
                if cnt: ret += 1
                j += 1
            
            while i < j:
                sl.add(prop[i][1])
                i += 1
        
        return ret
            