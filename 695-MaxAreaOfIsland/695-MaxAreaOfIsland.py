# Last updated: 12/6/2025, 5:47:37 am
class Union:
	def __init__(self, n):
		self.parents = [i for i in range(n)]
		self.size = [1] * n
		self.maxArea = 0
	
	def find(self, node):
		if node != self.parents[node]:
			self.parents[node] = self.find(self.parents[node])
		return self.parents[node]
	
	def union(self, node1, node2):
		root1 = self.find(node1)
		root2 = self.find(node2)

		if root1 == root2: return

		if self.size[root1] < self.size[root2]:
			root1, root2 = root2, root1
		
		self.parents[root2] = root1
		self.size[root1] += self.size[root2]
		self.maxArea = max(self.size[root1], self.maxArea)

class Solution:
	def maxAreaOfIsland(self, grid) -> int:
		m = len(grid)
		n = len(grid[0])
		uf = Union(m*n)
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1:
					pos = (i*n)+j
					uf.maxArea = max(uf.maxArea, 1)
					if i+1 < m and grid[i+1][j] == 1: uf.union(pos, pos+n)
					if j+1 < n and grid[i][j+1] == 1: uf.union(pos, pos+1)
		return uf.maxArea