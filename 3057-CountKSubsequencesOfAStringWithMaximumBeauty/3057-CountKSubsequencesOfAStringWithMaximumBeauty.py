# Last updated: 12/6/2025, 5:36:18 am
mod = 10**9 + 7
N = 10 ** 5 * 2 + 1

fact = [1] * N
inverses = [1] * N
for i in range(1, N):
    fact[i] = i * fact[i-1] % mod
    inverses[i] = pow(fact[i], -1, mod)

class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        uniq = {}
        for char in s:
            uniq[char] = 1
        
        if len(uniq) < k: return 0

        freq = [0] * 26

        for char in s:
            freq[ord(char) - 97] += 1
        
        arr = []
        for num in range(26):
            arr.append((freq[num], num))
        
        arr.sort(reverse=True)

        values = defaultdict(int)
        extras = defaultdict(int)

        for i in range(k):
            values[arr[i][0]] += 1
        
        for i in range(k, 26):
            extras[arr[i][0]] += 1

        ret = 1
        for _, index in arr[:k]:
            ret = ret * freq[index] % mod

        if k < 26 and arr[k][0] == arr[k-1][0]:
            rem = extras[arr[k][0]]
            cnt = values[arr[k][0]] + rem
            rem = cnt - rem

            ans = fact[cnt] * inverses[rem] * inverses[cnt-rem]
            ret = ret * ans % mod

        return ret
