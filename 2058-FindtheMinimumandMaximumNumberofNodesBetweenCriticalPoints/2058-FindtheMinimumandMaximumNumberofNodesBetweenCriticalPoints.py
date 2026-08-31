# Last updated: 8/31/2026, 4:30:44 PM
1class Solution:
2    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
3        node = head
4        prev = None
5        stack = []
6        index = -1
7        min_dis = inf
8        while node:
9            if prev and node.next:
10                if (node.val > prev.val and node.val > node.next.val) or (node.val < prev.val and node.val < node.next.val):
11                    if stack:
12                        prev_index = stack.pop()
13                        min_dis = min(index - prev_index, min_dis)
14
15                        if len(stack) == 0:
16                            stack.append(prev_index)
17                    stack.append(index)
18
19            index += 1
20            prev = node
21            node = node.next
22
23        if len(stack) < 2: return [-1, -1]
24        return [min_dis, stack[-1] - stack[0]]