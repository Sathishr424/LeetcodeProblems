# Last updated: 10/11/2026, 9:43:43 PM
1class Solution:
2    def threeFibonacciSum(self, n: int) -> bool:
3        fib = [0, 1]
4        while fib[-1] < n:
5            fib.append(fib[-1] + fib[-2])
6        return any(fib[i] + fib[i+1] + fib[i+2] == n for i in range(len(fib) - 2))
7