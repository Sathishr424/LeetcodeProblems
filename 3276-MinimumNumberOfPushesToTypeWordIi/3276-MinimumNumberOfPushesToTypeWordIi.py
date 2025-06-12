# Last updated: 12/6/2025, 5:35:54 am
class Solution:
    def minimumPushes(self, word: str) -> int:
        ret = 0
        hash = defaultdict(int)
        for char in word:
            hash[char] += 1
        
        if len(hash) <= 8: return len(word)

        arr = []
        for char in hash:
            arr.append(hash[char])
        
        arr.sort(reverse=True)
        curr = 1
        for i in range(len(arr)):
            ret += arr[i] * curr
            if (i+1) % 8 == 0:
                curr += 1
        return ret