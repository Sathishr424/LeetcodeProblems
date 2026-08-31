# Last updated: 8/31/2026, 4:31:58 PM
1class Solution:
2    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
3        node = head
4        prev = node
5        node = node.next
6
7        stack = []
8        index = -1
9        min_dis = inf
10
11        while node.next:
12            if (node.val > prev.val and node.val > node.next.val) or (node.val < prev.val and node.val < node.next.val):
13                if stack:
14                    prev_index = stack.pop()
15                    min_dis = min(index - prev_index, min_dis)
16
17                    if len(stack) == 0:
18                        stack.append(prev_index)
19                stack.append(index)
20
21            index += 1
22            prev = node
23            node = node.next
24
25        if len(stack) < 2: return [-1, -1]
26        return [min_dis, stack[-1] - stack[0]]