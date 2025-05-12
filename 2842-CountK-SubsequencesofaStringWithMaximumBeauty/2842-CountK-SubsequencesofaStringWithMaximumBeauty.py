# Last updated: 12/5/2025, 11:47:14 pm
# big_s = ''.join([chr(random.randrange(26) + 97) for _ in range(10**5 * 2)])
mod = 10**9 + 7
N = 10 ** 5 * 2 + 1

fact = [1] * N
inverses = [1] * N
for i in range(1, N):
    fact[i] = i * fact[i-1] % mod
    inverses[i] = pow(fact[i], -1, mod)


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        # s = big_s
        n = len(s)

        freq = [0] * 26
        
        nums = [ord(char) - 97 for char in s]
        uniq = {}
        for num in nums:
            uniq[num] = 1
            freq[num] += 1
        
        if len(uniq) < k: return 0

        # a, 25, b, 20,
        full_mask = (1 << 27) - 1
        start_mask = 1 << 26

        arr = []
        for num in range(26):
            arr.append((freq[num], num))
        
        arr.sort(reverse=True)
        max_score = 0

        values = defaultdict(int)

        for cnt, index in arr:
            values[cnt] += 1
        extras = defaultdict(int)
        for cnt, index in arr[k:]:
            extras[cnt] += 1

        # print(arr)
        curr = 1
        for num, index in arr[:k]:
            curr = curr * freq[index] % mod
        ret = curr
        # print(ret, k, arr[k-1:])
        if len(arr) > k and arr[k][0] == arr[k-1][0]:
            cnt = values[arr[k][0]]
            rem = cnt - extras[arr[k][0]]
            # print(cnt, rem)
            # ans = inverses[cnt] * (fact[rem] * fact[cnt-rem])
            ans = fact[cnt]
            ans *= inverses[rem]
            ans *= inverses[cnt-rem]

            curr = (curr * ans) % mod

        # "kjojr"
        #  12121
        # 2111
        # kjo, kjr, kjr, koj, jor, ojr

        return curr
