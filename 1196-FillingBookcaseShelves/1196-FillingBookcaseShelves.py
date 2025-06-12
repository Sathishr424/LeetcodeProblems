# Last updated: 12/6/2025, 5:43:41 am
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        dp = [float('inf')] * (n+1)
        dp[-1] = 0
        
        for i in range(n, -1, -1):
            height = 0
            width = 0
            for j in range(i, n):
                w, h = books[j]
                if width+w > shelfWidth:
                    dp[i] = min(dp[i], dp[j] + height)
                    break
                height = max(height, h)
                if width+w == shelfWidth:
                    dp[i] = min(dp[i], dp[j+1] + height)
                    break
                else:
                    width+= w
                    dp[i] = min(dp[i], dp[j+1] + height)
        
        return dp[0]