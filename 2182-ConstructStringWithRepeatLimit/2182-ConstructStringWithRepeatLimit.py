# Last updated: 26/8/2025, 1:04:15 am
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap = []

        counter = defaultdict(int)
        for char in s:
            counter[char] += 1

        heap = []
        for char in counter:
            heapq.heappush(heap, (-ord(char), counter[char], char))

        ret = ''
        while heap:
            a, cnt, char = heapq.heappop(heap)

            rem_cnt = max(0, cnt - repeatLimit)
            ret += char * min(repeatLimit, cnt)
            
            while rem_cnt and heap:
                a2, cnt2, char2 = heapq.heappop(heap)

                while rem_cnt and cnt2:
                    ret += char2
                    cnt2 -= 1

                    ret += char * min(repeatLimit, rem_cnt)
                    rem_cnt = max(0, rem_cnt - repeatLimit)
                
                if rem_cnt == 0 and cnt2:
                    heapq.heappush(heap, (a2, cnt2, char2))
        
        return ret