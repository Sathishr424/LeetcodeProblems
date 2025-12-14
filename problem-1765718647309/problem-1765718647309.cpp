// Last updated: 12/14/2025, 6:54:07 PM
1#include <bits/stdc++.h>
2#include <iostream>
3#include <vector>
4
5using namespace std;
6
7struct Node {
8    int cnt;
9    char left;
10    char right;
11
12    Node(char left, char right) {
13        this->left = left;
14        this->right = right;
15        this->cnt = 0;
16    }
17
18    Node() {
19        this->cnt = 0;
20        this->left = this->right = '-';
21    }
22};
23
24class SegmentTree {
25private:
26    int n;
27    vector<Node> tree;
28    string nums;
29public:
30    SegmentTree(string nums) {
31        this->nums = nums;
32        this->n = nums.size();
33
34        this->tree.resize(this->n * 4);
35        build(0, 0, this->n - 1);
36    }
37
38    Node build(int index, int left, int right) {
39        if (left == right) {
40            tree[index].left = nums[left];
41            tree[index].right = nums[right];
42            return tree[index];
43        }
44
45        int mid = (left + right) / 2;
46
47        Node left_node = build(index * 2 + 1, left, mid);
48        Node right_node = build(index * 2 + 2, mid + 1, right);
49
50        tree[index].cnt = left_node.cnt + right_node.cnt;
51        if (left_node.right == right_node.left) tree[index].cnt++;
52        tree[index].left = left_node.left;
53        tree[index].right = right_node.right;
54        return tree[index];
55    }
56
57    void update(int index, int left, int right, int update_index) {
58        if (left == right) {
59            tree[index].left = tree[index].left == 'A' ? 'B' : 'A';
60            tree[index].right = tree[index].left;
61            return;
62        }
63
64        int mid = (left + right) / 2;
65        if (update_index <= mid) {
66            update(index * 2 + 1, left, mid, update_index);
67        } else {
68            update(index * 2 + 2, mid + 1, right, update_index);
69        }
70        Node& left_node = tree[index * 2 + 1];
71        Node& right_node = tree[index * 2 + 2];
72
73        tree[index].cnt = left_node.cnt + right_node.cnt;
74        if (left_node.right == right_node.left) tree[index].cnt++;
75        tree[index].left = left_node.left;
76        tree[index].right = right_node.right;
77    }
78
79    Node query(int index, int l, int r, int left, int right) {
80        if (l > right || r < left) return Node();
81
82        if (l >= left && r <= right) {
83            return tree[index];
84        }
85
86        int mid = (l + r) / 2;
87        Node left_node = query(index * 2 + 1, l, mid, left, right);
88        Node right_node = query(index * 2 + 2, mid + 1, r, left, right);
89
90        if (left_node.left != '-' && right_node.right != '-') {
91            Node new_node = Node();
92            new_node.cnt = left_node.cnt + right_node.cnt;
93            if (left_node.right == right_node.left) new_node.cnt++;
94            new_node.left = left_node.left;
95            new_node.right = right_node.right;
96            return new_node;
97        }
98        if (left_node.left != '-') {
99            return left_node;
100        }
101        return right_node;
102    }
103};
104
105class Solution {
106public:
107    vector<int> minDeletions(string s, vector<vector<int>>& queries) {
108        int n = s.length();
109        SegmentTree segTree = SegmentTree(s);
110
111        vector<int> ret;
112
113        for (auto& q: queries) {
114            if (q[0] == 1) {
115                segTree.update(0, 0, n-1, q[1]);
116            } else {
117                Node node = segTree.query(0, 0, n-1, q[1], q[2]);
118                ret.push_back(node.cnt);
119            }
120        }
121
122        return ret;
123    }
124};