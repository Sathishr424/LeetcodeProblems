# Last updated: 12/6/2025, 5:49:46 am
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heights = defaultdict(list)
        n = len(people)
        people.sort(reverse=True)

        for x, y in people:
            heights[y].append(x)

        ret = []
        helper = SortedList()

        def bn(val):
            l = 0
            r = len(helper)

            while l < r:
                mid = (l+r) // 2

                if helper[mid] >= val:
                    r = mid
                else:
                    l = mid+1
            
            return len(helper)-l

        def rec(height):
            if len(ret) == n: return ret

            h = height
            while h > 0 and (len(heights[h]) == 0 or bn(heights[h][-1]) != h):
                h -= 1

            x = heights[h].pop()
            helper.add(x)
            ret.append([x, h])
            
            return rec(height+1)

        return rec(0)