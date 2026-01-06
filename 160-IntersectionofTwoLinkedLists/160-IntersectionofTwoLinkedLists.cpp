// Last updated: 1/6/2026, 9:53:16 PM
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
15    // cout << m << " " << n << " " << diff << endl;
16    // cout << m << " " << n << " " << endl;
17
18    if (n > m) {
19      ListNode *tmp = headA;
20      headA = headB;
21      headB = tmp;
22      n ^= m;
23      m ^= n;
24      n ^= m;
25    }
26    int diff = m - n;
27
28    while (diff--) {
29      headA = headA->next;
30    }
31
32    while (headA) {
33      if (headA == headB)
34        return headA;
35      headA = headA->next;
36      headB = headB->next;
37    }
38
39    return nullptr;
40  }
41};