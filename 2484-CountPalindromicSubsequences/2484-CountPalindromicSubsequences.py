# Last updated: 11/5/2025, 4:30:37 pm
big_s = ''.join([str(random.randrange(0, 10)) for _ in range(10**4)])
index = 0
relation = {}
index_to_relation = [''] * 100
opp_relation_index = [0] * 100

for i in range(10):
    val = '0' + str(i)
    op = val[::-1]
    relation[val] = index
    index_to_relation[index] = val
    
    index += 1

for i in range(10, 100):
    val = str(i)
    op = val[::-1]
    
    relation[str(i)] = index
    index_to_relation[index] = str(i)
    index += 1

for num in relation:
    opp_relation_index[relation[num]] = relation[num[::-1]]

mod = 10**9 + 7

pre = [[''] * 10 for _ in range(10)]

for i in range(10):
    for j in range(10):
        pre[i][j] = str(i) + str(j)

class Solution:
    def countPalindromes(self, s: str) -> int:
        # s = big_s
        n = len(s)
        ret = 0
        freq = [0] * 10
        arr = [int(i) for i in s]

        dp = [[0] * 100]
        
        freq[arr[0]] += 1
        for i in range(1, n):
            dp.append(dp[-1] + [])
            val = arr[i]
            for num in range(10):
                if freq[num] > 0:
                    y = pre[num][val]
                    dp[i][relation[y]] += freq[num]

            freq[val] += 1

        freq = [0] * 10
        right_dp = [0] * 100
        for i in range(n-1, 1, -1):
            
            if i < n-2:
                for index in range(100):
                    left = dp[i-1][opp_relation_index[index]]
                    right = right_dp[index]
                    if left and right:
                        ret = (ret + left * right % mod) % mod

            val = arr[i]
            for num in range(10):
                if freq[num] > 0:
                    y = pre[val][num]
                    right_dp[relation[y]] += freq[num]
        
            freq[val] += 1
        
        return ret % mod
