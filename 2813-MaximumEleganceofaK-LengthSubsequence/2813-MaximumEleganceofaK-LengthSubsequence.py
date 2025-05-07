# Last updated: 7/5/2025, 11:11:54 pm
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        n = len(items)
        items.sort(key=lambda x: x[0], reverse=True)

        uniq = defaultdict(int)
        total = 0

        for i in range(k):
            total += items[i][0]
            uniq[items[i][1]] += 1
        
        ret = total + (len(uniq) ** 2)
        profits = []

        for i in range(k):
            if uniq[items[i][1]] > 1:
                heapq.heappush(profits, (items[i][0], i))
        
        # print(items)
        # print(profits)

        for i in range(k, n):
            if items[i][1] not in uniq:
                while profits and uniq[ items[profits[0][1]][1] ] == 1:
                    heapq.heappop(profits)
                
                if not profits: break

                profit, index = heapq.heappop(profits)

                uniq[items[index][1]] -= 1

                total -= profit
                total += items[i][0]
                
                uniq[items[i][1]] += 1
                ret = max(ret, total + (len(uniq) ** 2))

                # print(items[i], ret, (profit, index), len(uniq), total, ret)
            
        return ret