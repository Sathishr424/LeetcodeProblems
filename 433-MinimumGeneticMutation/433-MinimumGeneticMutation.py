# Last updated: 12/6/2025, 5:49:33 am
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        options = ['A', 'C', 'G', 'T']
        banks = {}
        for b in bank: banks[b] = 1

        stack = [startGene]
        steps = 0
        visited = {}

        while stack:
            new_stack = []

            for gene in stack:
                for i in range(8):
                    for o in options:
                        g = gene[:i] + o + gene[i+1:]
                        if g in banks and g not in visited:
                            if g == endGene: return steps + 1
                            new_stack.append(g)
                            visited[g] = 1
            
            steps += 1
            stack = new_stack
        
        return -1