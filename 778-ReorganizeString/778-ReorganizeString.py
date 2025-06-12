# Last updated: 12/6/2025, 5:46:55 am
class Solution:
    def reorganizeString(self, s: str) -> str:
        hash = defaultdict(lambda: 0)
        for i in s: hash[i] += 1

        arr = []
        for k in hash:
            arr.append([-hash[k], k])
        heapq.heapify(arr)
        last = ""
        ret = ""
        while arr:
            val = ""
            if arr[0][1] == last:
                if len(arr) > 1:
                    val = heapq.heappop(arr)
                    left = arr[0]
                    ret += left[1]
                    last = left[1]

                    if left[0]+1 == 0:
                        heapq.heapreplace(arr, val)
                    else:
                        left[0] += 1
                        heapq.heappush(arr, val)
                else: return ""
            else:
                left = arr[0]
                ret += left[1]
                last = left[1]

                if left[0]+1 == 0:
                    heapq.heappop(arr)
                else:
                    left[0] += 1
                    heapq.heapify(arr)
        return ret


        
