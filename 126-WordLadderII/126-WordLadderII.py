# Last updated: 21/7/2025, 9:24:01 pm
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        there = defaultdict(list)
        m = len(beginWord)
        possible = defaultdict(list)
        for word in wordList:
            for i in range(m):
                new_word = word[:i] + "*" + word[i+1:]
                there[new_word].append(word)
                possible[word].append(new_word)
        
        if beginWord not in possible:
            for i in range(m):
                new_word = beginWord[:i] + "*" + beginWord[i+1:]
                there[new_word].append(beginWord)
                possible[beginWord].append(new_word)
        
        ret = []      
        def addItoRet(index, arr, s):
            if index == len(arr):
                ret.append(s + [endWord])
                return
            for word in there[arr[index]]:
                if word not in s:
                    s.append(word)
                    addItoRet(index + 1, arr, s)
                    s.pop()      
        
        stack = deque([(beginWord, 1)])
        can_visit = {}
        visited = {}
        shortest = inf
        while stack:
            word, cnt = stack.popleft()
            if word in visited and visited[word] <= cnt: continue
            visited[word] = cnt
            can_visit[word] = 1
            if word == endWord:
                shortest = cnt
                break

            for new_word in possible[word]:
                for n_word in there[new_word]:
                    stack.append((n_word, cnt + 1))
        
        if shortest == inf: return []

        visited = {}
        def dfs(word, s):
            if word == beginWord:
                ret.append(s[::-1])
                return
            if len(s) == shortest: return
            for new_word in possible[word]:
                for n_word in there[new_word]:
                    if n_word not in can_visit or n_word in visited: continue
                    visited[n_word] = 1
                    s.append(n_word)
                    dfs(n_word, s)
                    s.pop()
                    del visited[n_word]
        dfs(endWord, [endWord])
        return ret