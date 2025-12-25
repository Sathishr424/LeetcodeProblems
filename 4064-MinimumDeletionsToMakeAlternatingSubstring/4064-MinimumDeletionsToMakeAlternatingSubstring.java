// Last updated: 12/25/2025, 7:08:35 PM
import java.util.ArrayList;
import java.util.List;

class Node {
    public char left;
    public char right;
    public int cnt;

    public Node() {
        this.left = '-';
        this.right = '-';
        this.cnt = 0;
    }
}

class SegmentTree {
    private final int n;
    private final Node[] tree;
    private final String str;

    public SegmentTree(String str) {
        this.n = str.length();
        this.str = str;
        tree = new Node[n * 4];
        for (int i=0; i<n * 4; i++) {
            tree[i] = new Node();
        }
        build(0, 0, n-1);
    }

    public Node build(int index, int l, int r) {
        if (l == r) {
            tree[index].left = tree[index].right = str.charAt(l);
            return tree[index];
        }

        int mid = (l + r) / 2;
        Node left_node = build(index * 2 + 1, l, mid);
        Node right_node = build(index * 2 + 2, mid + 1, r);

        tree[index].cnt = left_node.cnt + right_node.cnt;
        tree[index].left = left_node.left;
        tree[index].right = right_node.right;
        if (left_node.right == right_node.left) tree[index].cnt++;
        return tree[index];
    }

    private void update(int index, int l, int r, int update_index) {
        if (l == r) {
            tree[index].left = tree[index].right = tree[index].left == 'A' ? 'B' : 'A';
            return;
        }

        int mid = (l + r) / 2;
        if (update_index <= mid) {
            update(index * 2 + 1, l, mid, update_index);
        } else {
            update(index * 2 + 2, mid + 1, r, update_index);
        }

        Node left_node = tree[index * 2 + 1];
        Node right_node = tree[index * 2 + 2];

        tree[index].cnt = left_node.cnt + right_node.cnt;
        tree[index].left = left_node.left;
        tree[index].right = right_node.right;
        if (left_node.right == right_node.left) tree[index].cnt++;
    }

    public void flip(int index) {
        update(0, 0, n-1, index);
    }

    private Node query(int index, int l, int r, int left, int right) {
        if (l > right || r < left) return new Node();

        if (l >= left && r <= right) return tree[index];
        int mid = (l + r) / 2;

        Node left_node = query(index * 2 + 1, l, mid, left, right);
        Node right_node = query(index * 2 + 2, mid + 1, r, left, right);

        if (left_node.left != '-' && right_node.left != '-') {
            Node new_node = new Node();
            new_node.cnt = left_node.cnt + right_node.cnt;
            new_node.left = left_node.left;
            new_node.right = right_node.right;
            if (left_node.right == right_node.left) new_node.cnt++;
            return new_node;
        }
        if (left_node.left != '-') return left_node;
        return right_node;
    }

    public int minDeletions(int l, int r) {
        return query(0, 0, n-1, l, r).cnt;
    }
}

public class Solution {
    public int[] minDeletions(String s, int[][] queries) {
        SegmentTree segTree = new SegmentTree(s);
        List<Integer> res = new ArrayList<>();
        for (int[] query : queries) {
            if (query[0] == 1) {
                segTree.flip(query[1]);
            } else {
                res.add(segTree.minDeletions(query[1], query[2]));
            }
        }

        return res.stream().mapToInt(Integer::intValue).toArray();
    }
}