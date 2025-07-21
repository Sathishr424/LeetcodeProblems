# Last updated: 21/7/2025, 5:37:29 pm
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        there = defaultdict(list)
        m = len(beginWord)
        for word in wordList:
            for i in range(m):
                new_word = word[:i] + "*" + word[i+1:]
                there[new_word].append(word)
        
        stack = deque([(beginWord, 1)])
        visited = {}
        while stack:
            word, cnt = stack.popleft()
            if word in visited and visited[word] <= cnt: continue
            visited[word] = cnt
            if word == endWord:
                return cnt

            for i in range(m):
                new_word = word[:i] + "*" + word[i+1:]
                for n_word in there[new_word]:
                    stack.append((n_word, cnt + 1))
        
        return 0