# Last updated: 12/25/2025, 7:10:31 PM
class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        tree = [defaultdict(int) for _ in range(n * 4)]
        indexes = [0] * n
        prev_pop_cnts = [0] * n

        def getPopCount(num):
            if num == 1: return 0
            cnt = 0
            while num:
                if num % 2:
                    cnt += 1
                num //= 2
            return getPopCount(cnt) + 1

        def build(l, r, index):
            if l == r:
                indexes[l] = index
                cnt = getPopCount(nums[l])
                prev_pop_cnts[l] = cnt
                tree[index][cnt] += 1
                return tree[index]

            mid = (l + r) // 2
            left = build(l, mid, index * 2 + 1)
            right = build(mid + 1, r, index * 2 + 2)
            for num in left:
                tree[index][num] += left[num]
            
            for num in right:
                tree[index][num] += right[num]
            return tree[index]
        build(0, n-1, 0)
        def query(l, r, left, right, index, k):
            if r < left or l > right:
                return 0

            if l >= left and r <= right:
                return tree[index][k]

            mid = (l + r) // 2
            ans = query(l, mid, left, right, index * 2 + 1, k)
            ans += query(mid + 1, r, left, right, index * 2 + 2, k)
            return ans

        def update(i, num):
            index = indexes[i]
            prev = prev_pop_cnts[i]
            tree[index][prev] -= 1
            
            cnt = getPopCount(num)
            prev_pop_cnts[i] = cnt
            tree[index][cnt] += 1
            while index:
                index = (index - 1) // 2
                
                tree[index][prev] -= 1
                tree[index][cnt] += 1
        
        ret = []
        for i in range(len(queries)):
            q = queries[i]
            if q[0] == 1:
                ans = query(0, n-1, q[1], q[2], 0, q[3])
                ret.append(ans)
            else:
                update(q[1], q[2])

        return ret
            