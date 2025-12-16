// Last updated: 12/16/2025, 2:33:07 PM
1import java.util.ArrayList;
2import java.util.List;
3
4class Node {
5    public char left;
6    public char right;
7    public int cnt;
8
9    public Node() {
10        this.left = '-';
11        this.right = '-';
12        this.cnt = 0;
13    }
14}
15
16class SegmentTree {
17    private final int n;
18    private final Node[] tree;
19    private final String str;
20
21    public SegmentTree(String str) {
22        this.n = str.length();
23        this.str = str;
24        tree = new Node[n * 4];
25        for (int i=0; i<n * 4; i++) {
26            tree[i] = new Node();
27        }
28        build(0, 0, n-1);
29    }
30
31    public Node build(int index, int l, int r) {
32        if (l == r) {
33            tree[index].left = tree[index].right = str.charAt(l);
34            return tree[index];
35        }
36
37        int mid = (l + r) / 2;
38        Node left_node = build(index * 2 + 1, l, mid);
39        Node right_node = build(index * 2 + 2, mid + 1, r);
40
41        tree[index].cnt = left_node.cnt + right_node.cnt;
42        tree[index].left = left_node.left;
43        tree[index].right = right_node.right;
44        if (left_node.right == right_node.left) tree[index].cnt++;
45        return tree[index];
46    }
47
48    private void update(int index, int l, int r, int update_index) {
49        if (l == r) {
50            tree[index].left = tree[index].right = tree[index].left == 'A' ? 'B' : 'A';
51            return;
52        }
53
54        int mid = (l + r) / 2;
55        if (update_index <= mid) {
56            update(index * 2 + 1, l, mid, update_index);
57        } else {
58            update(index * 2 + 2, mid + 1, r, update_index);
59        }
60
61        Node left_node = tree[index * 2 + 1];
62        Node right_node = tree[index * 2 + 2];
63
64        tree[index].cnt = left_node.cnt + right_node.cnt;
65        tree[index].left = left_node.left;
66        tree[index].right = right_node.right;
67        if (left_node.right == right_node.left) tree[index].cnt++;
68    }
69
70    public void flip(int index) {
71        update(0, 0, n-1, index);
72    }
73
74    private Node query(int index, int l, int r, int left, int right) {
75        if (l > right || r < left) return new Node();
76
77        if (l >= left && r <= right) return tree[index];
78        int mid = (l + r) / 2;
79
80        Node left_node = query(index * 2 + 1, l, mid, left, right);
81        Node right_node = query(index * 2 + 2, mid + 1, r, left, right);
82
83        if (left_node.left != '-' && right_node.left != '-') {
84            Node new_node = new Node();
85            new_node.cnt = left_node.cnt + right_node.cnt;
86            new_node.left = left_node.left;
87            new_node.right = right_node.right;
88            if (left_node.right == right_node.left) new_node.cnt++;
89            return new_node;
90        }
91        if (left_node.left != '-') return left_node;
92        return right_node;
93    }
94
95    public int minDeletions(int l, int r) {
96        return query(0, 0, n-1, l, r).cnt;
97    }
98}
99
100public class Solution {
101    public int[] minDeletions(String s, int[][] queries) {
102        SegmentTree segTree = new SegmentTree(s);
103        List<Integer> res = new ArrayList<>();
104        for (int[] query : queries) {
105            if (query[0] == 1) {
106                segTree.flip(query[1]);
107            } else {
108                res.add(segTree.minDeletions(query[1], query[2]));
109            }
110        }
111
112        return res.stream().mapToInt(Integer::intValue).toArray();
113    }
114}