# Last updated: 28/10/2025, 2:33:00 am
class Solution:
    def maximizeWin(self, price: List[int], k: int) -> int:
        n = len(price)

        prefix = []
        for i in range(n):
            num = price[i]
            right = bisect_right(price, num + k) - 1
            prefix.append(right)
            
        right_max = [0] * (n + 1)
        right_max[n-1] = 1
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i + 1], prefix[i] - i + 1)
        
        def getCan(mid, right):
            l = mid
            r = prefix[mid]

            diff = max(0, right - l + 1)

            can = r - l + 1
            return max(0, can - diff)

        best = 0
        for i in range(n):
            num = price[i]
            right = prefix[i]
            tot = right - i + 1
            
            l = i
            r = right

            while l < r:
                mid = (l + r) // 2
                # print(i, (l, mid, r))

                if getCan(mid, right) > getCan(mid + 1, right):
                    r = mid
                else:
                    l = mid + 1

            # print(i, l, '-', (i, right), (l, prefix[l]), tot, getCan(l, right), tot + getCan(l, right))
            best = max(best, tot + getCan(l, right))
            best = max(best, tot + right_max[right + 1])

        return best

                