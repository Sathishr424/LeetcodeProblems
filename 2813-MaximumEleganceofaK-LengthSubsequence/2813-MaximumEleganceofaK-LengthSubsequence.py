# Last updated: 7/5/2025, 11:25:21 pm
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        n = len(items)
        items.sort(key=lambda x: x[0], reverse=True)

        uniq = defaultdict(int)
        total = 0
        stack = []

        for i in range(k):
            total += items[i][0]
            uniq[items[i][1]] += 1

            if uniq[items[i][1]] > 1:
                stack.append(items[i])

        ret = total + (len(uniq) ** 2)

        for i in range(k, n):
            if items[i][1] not in uniq:
                while stack and uniq[ stack[-1][1] ] == 1:
                    stack.pop()
                
                if not stack: break

                profit, cat = stack.pop()

                uniq[ cat ] -= 1

                total -= profit
                total += items[i][0]
                
                uniq[items[i][1]] += 1

                ret = max(ret, total + (len(uniq) ** 2))
            
        return ret