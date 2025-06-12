# Last updated: 12/6/2025, 5:52:41 am
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        m = len(beginWord)

        # wordMatch = defaultdict(list)

        # for word in wordList:
        #     for i in range(m):
        #         w = word[:i] + '*' + word[i+1:]
        #         wordMatch[w].append(word)

        wordMatch = {}

        for word in wordList:
            wordMatch[word] = 1
        
        visited = {}
        stack = deque([(beginWord, 1)])
        visited[beginWord] = 1

        while stack:
            word, cnt = stack.popleft()
            if word == endWord: return cnt

            for i in range(m):
                for j in range(26):
                    w = word[:i] + chr(97+j) + word[i+1:]
                    if w == word: continue
                    if w in wordMatch and w not in visited:
                        stack.append((w, cnt+1))
                        visited[w] = 1

        return 0
            