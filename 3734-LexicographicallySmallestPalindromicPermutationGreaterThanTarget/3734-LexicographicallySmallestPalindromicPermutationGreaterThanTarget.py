# Last updated: 2/11/2025, 9:36:21 am
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        target_a = [ord(char) - ord('a') for char in target]
        orig_freq = [0] * 26

        for char in s:
            orig_freq[ord(char) - ord('a')] += 1

        odd = ''
        for a in range(26):
            if orig_freq[a] == 0: continue
            char = chr(a + ord('a'))
            if orig_freq[a] % 2:
                if odd != '': return ""
                odd = char
            orig_freq[a] //= 2

        stack = deque([("", 0, orig_freq[:], True)])
        def_ans = 'z' * (n + 1)
        ans = def_ans
        while stack:
            t, index, freq, strict = stack.popleft()
            if not strict:
                # print(index, t, freq)
                right = ''
                for i in range(26):
                    if freq[i]:
                        right += chr(i + ord('a')) * freq[i]
                t += right
                t = t + odd + t[::-1]
                if t < ans: ans = t
                continue
            
            # print(t, index, freq)
            if index == n//2:
                new_t = t + odd + t[::-1]
                if new_t > target and new_t < ans: 
                    ans = new_t 
                continue

            for i in range(26):
                if freq[i] == 0: continue
                if not strict or i >= target_a[index]:
                    char = chr(i + ord('a'))
                    new_freq = freq[:]
                    new_freq[i] -= 1
                    stack.append((t + char, index + 1, new_freq, strict and i == target_a[index]))

        if ans != def_ans: return ans
        return ''