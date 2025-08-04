# Last updated: 4/8/2025, 2:10:16 pm
class Solution:
    def totalFruit(self, f: List[int]) -> int:
        n = len(f)
        ret = 1

        freq = defaultdict(int)
        cnt = 0
        left = 0

        for i in range(n):
            freq[f[i]] += 1
            if freq[f[i]] == 1:
                cnt += 1
            
            while cnt > 2:
                freq[f[left]] -= 1
                if freq[f[left]] == 0:
                    cnt -= 1
                left += 1

            # print(freq, left, cnt, i)
            ret = max(ret, i - left + 1)

        return ret 