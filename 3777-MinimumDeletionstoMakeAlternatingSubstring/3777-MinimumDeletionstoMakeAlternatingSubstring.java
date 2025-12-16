// Last updated: 12/16/2025, 2:29:11 PM
1import java.util.ArrayList;
2import java.util.List;
3
4class Node {
5    public char left;
6    public char right;
7    public int cnt;
8
9    public Node(char left, char right, int cnt) {
10        this.left = left;
11        this.right = right;
12    }
13
14    public Node() {
15        this.left = '-';
16        this.right = '-';
17        this.cnt = 0;
18    }
19}
20
21class SegmentTree {
22    private final int n;
23    private final Node[] tree;
24    private final String str;
25
26    public SegmentTree(String str) {
27        this.n = str.length();
28        this.str = str;
29        tree = new Node[n * 4];
30        for (int i=0; i<n * 4; i++) {
31            tree[i] = new Node();
32        }
33        build(0, 0, n-1);
34    }
35
36    public Node build(int index, int l, int r) {
37        if (l == r) {
38            tree[index].left = tree[index].right = str.charAt(l);
39            return tree[index];
40        }
41
42        int mid = (l + r) / 2;
43        Node left_node = build(index * 2 + 1, l, mid);
44        Node right_node = build(index * 2 + 2, mid + 1, r);
45
46        tree[index].cnt = left_node.cnt + right_node.cnt;
47        tree[index].left = left_node.left;
48        tree[index].right = right_node.right;
49        if (left_node.right == right_node.left) tree[index].cnt++;
50        return tree[index];
51    }
52
53    private void update(int index, int l, int r, int update_index) {
54        if (l == r) {
55            tree[index].left = tree[index].right = tree[index].left == 'A' ? 'B' : 'A';
56            return;
57        }
58
59        int mid = (l + r) / 2;
60        if (update_index <= mid) {
61            update(index * 2 + 1, l, mid, update_index);
62        } else {
63            update(index * 2 + 2, mid + 1, r, update_index);
64        }
65
66        Node left_node = tree[index * 2 + 1];
67        Node right_node = tree[index * 2 + 2];
68
69        tree[index].cnt = left_node.cnt + right_node.cnt;
70        tree[index].left = left_node.left;
71        tree[index].right = right_node.right;
72        if (left_node.right == right_node.left) tree[index].cnt++;
73    }
74
75    public void flip(int index) {
76        update(0, 0, n-1, index);
77    }
78
79    private Node query(int index, int l, int r, int left, int right) {
80        if (l > right || r < left) return new Node();
81
82        if (l >= left && r <= right) return tree[index];
83        int mid = (l + r) / 2;
84
85        Node left_node = query(index * 2 + 1, l, mid, left, right);
86        Node right_node = query(index * 2 + 2, mid + 1, r, left, right);
87
88        if (left_node.left != '-' && right_node.left != '-') {
89            Node new_node = new Node();
90            new_node.cnt = left_node.cnt + right_node.cnt;
91            new_node.left = left_node.left;
92            new_node.right = right_node.right;
93            if (left_node.right == right_node.left) new_node.cnt++;
94            return new_node;
95        }
96        if (left_node.left != '-') return left_node;
97        return right_node;
98    }
99
100    public int minDeletions(int l, int r) {
101        return query(0, 0, n-1, l, r).cnt;
102    }
103}
104
105public class Solution {
106    public int[] minDeletions(String s, int[][] queries) {
107        SegmentTree segTree = new SegmentTree(s);
108        List<Integer> res = new ArrayList<>();
109        for (int[] query : queries) {
110            if (query[0] == 1) {
111                segTree.flip(query[1]);
112            } else {
113                res.add(segTree.minDeletions(query[1], query[2]));
114            }
115        }
116
117        return res.stream().mapToInt(Integer::intValue).toArray();
118    }
119}