# Last updated: 6/11/2025, 1:18:24 am
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ret = []

        indexes = defaultdict(list)

        for i in range(n):
            indexes[nums[i]].append(i)

        s = 0
        extra = 0
        freq = defaultdict(int)
        left = []
        right = []
        left_there = set()

        # print(indexes)

        def withinBounds(num, cnt, index, left_limit):
            # return index > left_limit
            num_index = bisect_left(indexes[num], index)
            # print(num, cnt, (index, num_index), left_limit)
            return indexes[num][num_index - cnt + 1] > left_limit

        def go(i):
            nonlocal s, extra
            num = nums[i]

            if num in left_there:
                s -= num * freq[num]
                left_there.discard(num)
                extra += 1
            
            freq[num] += 1
            heapq.heappush(right, (-freq[num], -num, i))

            while left and (freq[left[0][1]] != left[0][0] or not withinBounds(left[0][1], left[0][0], left[0][2], i - k)):
                heapq.heappop(left)
                extra -= 1
            
            while right and (len(left) - extra < x or ( -right[0][0] > left[0][0] or ( -right[0][0] == left[0][0] and -right[0][1] > left[0][1] ) ) ):
                if freq[-right[0][1]] != -right[0][0] or not withinBounds(-right[0][1], -right[0][0], right[0][2], i - k):
                    heapq.heappop(right)
                    continue
                c, num, index = heapq.heappop(right)
                c = -c
                num = -num
                heapq.heappush(left, (c, num, index))
                left_there.add(num)
                s += num * c

            while len(left) - extra > x:
                c, num, index = heapq.heappop(left)
                if freq[num] != c or not withinBounds(num, c, index, i - k):
                    extra -= 1
                else:
                    heapq.heappush(right, (-c, -num, index))
                    if freq[num] == c:
                        s -= num * c
                    left_there.discard(num)
                
            # print(i, s, extra, left, right, dict(freq))
    
        for i in range(k):
            go(i)
        
        ret.append(s)

        for i in range(k, n):
            prev_num = nums[i - k]
            if prev_num in left_there:
                extra += 1
                s -= prev_num * freq[prev_num]
                left_there.discard(prev_num)
            
            freq[prev_num] -= 1
            if freq[prev_num]:
                # index = i
                index = bisect_right(indexes[prev_num], i)
                index = indexes[prev_num][index - 1]
                heapq.heappush(right, (-freq[prev_num], -prev_num, index))

            go(i)
            
            ret.append(s)

        return ret