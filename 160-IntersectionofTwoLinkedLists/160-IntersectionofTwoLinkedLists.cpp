// Last updated: 1/6/2026, 9:56:06 PM
1class Solution {
2public:
3  ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
4    int m = 0, n = 0;
5    ListNode *node = headA;
6    while (node) {
7      node = node->next;
8      m++;
9    }
10    node = headB;
11    while (node) {
12      node = node->next;
13      n++;
14    }
15
16    if (n > m) {
17      ListNode *tmp = headA;
18      headA = headB;
19      headB = tmp;
20      n ^= m;
21      m ^= n;
22      n ^= m;
23    }
24    int diff = m - n;
25
26    while (diff--) {
27      headA = headA->next;
28    }
29
30    while (headA) {
31      if (headA == headB)
32        return headA;
33      headA = headA->next;
34      headB = headB->next;
35    }
36
37    return nullptr;
38  }
39};