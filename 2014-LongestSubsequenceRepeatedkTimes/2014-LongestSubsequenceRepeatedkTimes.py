# Last updated: 27/6/2025, 6:11:58 pm
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        indexes = defaultdict(deque)

        for i, char in enumerate(s):
            indexes[char].append(i)
        
        ret = ''
        char_limit = n // k

        candidates = []
        used = {}
        for char in s:
            if char not in used and len(indexes[char]) >= k:
                candidates.append(char)
                used[char] = 1
        
        visited = {}
        def check(st, used):
            if len(st) > char_limit: return
            if st in visited: return
            visited[st] = 1
            for char in candidates:
                if (used[char] + 1) * k <= len(indexes[char]):
                    used[char] += 1
                    check(st + char, used)
                    used[char] -= 1
        
        check('', defaultdict(int))
        # print(visited)

        def check_possible(st):
            # print(st)
            last_index = -1
            for i in range(k):
                for char in st:
                    l_index = bisect_left(indexes[char], last_index + 1)
                    if l_index == len(indexes[char]):
                        return False
                    last_index = indexes[char][l_index]
            return True

        for st in sorted(visited.keys(), key=lambda x: (len(x), x), reverse=True):
            if check_possible(st):
                ret = st
                break
        
        return ret
            
