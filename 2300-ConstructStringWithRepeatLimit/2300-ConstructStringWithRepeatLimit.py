# Last updated: 12/6/2025, 5:38:30 am
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        hash = defaultdict(int)
        for char in s:
            hash[char] += 1
        arr = []
        for key in hash:
            arr.append((key, hash[key]))
        
        arr.sort(key=lambda x: x[0])
        prev = ''
        cnt = 0
        ret = ''
        while arr:
            char, rem = arr.pop()
            if char == prev:
                if cnt+1 <= repeatLimit:
                    ret += char
                    cnt += 1
                    rem -= 1
                else:
                    if arr:
                        n_char, n_rem = arr.pop()
                        ret += n_char
                        prev = n_char
                        cnt = 1
                        n_rem -= 1
                        if n_rem > 0: arr.append((n_char, n_rem))
                    else:
                        break
            else:
                ret += char
                cnt = 1
                prev = char
                rem -= 1
            if rem > 0: arr.append((char, rem))

        return ret

