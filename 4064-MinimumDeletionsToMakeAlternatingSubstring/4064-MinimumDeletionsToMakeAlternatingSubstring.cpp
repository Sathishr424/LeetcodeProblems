// Last updated: 12/25/2025, 7:08:41 PM
#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;

struct Node {
    int cnt;
    char left;
    char right;

    Node(char left, char right) {
        this->left = left;
        this->right = right;
        this->cnt = 0;
    }

    Node() {
        this->cnt = 0;
        this->left = this->right = '-';
    }
};

class SegmentTree {
private:
    int n;
    vector<Node> tree;
    string nums;
public:
    SegmentTree(string nums) {
        this->nums = nums;
        this->n = nums.size();

        this->tree.resize(this->n * 4);
        build(0, 0, this->n - 1);
    }

    Node build(int index, int left, int right) {
        if (left == right) {
            tree[index].left = nums[left];
            tree[index].right = nums[right];
            return tree[index];
        }

        int mid = (left + right) / 2;

        Node left_node = build(index * 2 + 1, left, mid);
        Node right_node = build(index * 2 + 2, mid + 1, right);

        tree[index].cnt = left_node.cnt + right_node.cnt;
        if (left_node.right == right_node.left) tree[index].cnt++;
        tree[index].left = left_node.left;
        tree[index].right = right_node.right;
        return tree[index];
    }

    void update(int index, int left, int right, int update_index) {
        if (left == right) {
            tree[index].left = tree[index].left == 'A' ? 'B' : 'A';
            tree[index].right = tree[index].left;
            return;
        }

        int mid = (left + right) / 2;
        if (update_index <= mid) {
            update(index * 2 + 1, left, mid, update_index);
        } else {
            update(index * 2 + 2, mid + 1, right, update_index);
        }
        Node& left_node = tree[index * 2 + 1];
        Node& right_node = tree[index * 2 + 2];

        tree[index].cnt = left_node.cnt + right_node.cnt;
        if (left_node.right == right_node.left) tree[index].cnt++;
        tree[index].left = left_node.left;
        tree[index].right = right_node.right;
    }

    Node query(int index, int l, int r, int left, int right) {
        if (l > right || r < left) return Node();

        if (l >= left && r <= right) {
            return tree[index];
        }

        int mid = (l + r) / 2;
        Node left_node = query(index * 2 + 1, l, mid, left, right);
        Node right_node = query(index * 2 + 2, mid + 1, r, left, right);

        if (left_node.left != '-' && right_node.right != '-') {
            Node new_node = Node();
            new_node.cnt = left_node.cnt + right_node.cnt;
            if (left_node.right == right_node.left) new_node.cnt++;
            new_node.left = left_node.left;
            new_node.right = right_node.right;
            return new_node;
        }
        if (left_node.left != '-') {
            return left_node;
        }
        return right_node;
    }
};

class Solution {
public:
    vector<int> minDeletions(string s, vector<vector<int>>& queries) {
        int n = s.length();
        SegmentTree segTree = SegmentTree(s);

        vector<int> ret;

        for (auto& q: queries) {
            if (q[0] == 1) {
                segTree.update(0, 0, n-1, q[1]);
            } else {
                Node node = segTree.query(0, 0, n-1, q[1], q[2]);
                ret.push_back(node.cnt);
            }
        }

        return ret;
    }
};