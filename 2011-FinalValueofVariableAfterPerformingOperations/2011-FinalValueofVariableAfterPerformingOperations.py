# Last updated: 20/10/2025, 11:49:03 am
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        n = len(operations)

        x = 0
        for op in operations:
            if op == "X++" or op == "++X":
                x += 1
            elif op == "X--" or op == "--X":
                x -= 1
        
        return x