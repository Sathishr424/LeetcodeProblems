// Last updated: 4/9/2025, 4:02:10 pm
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int maxLen = 1;
    int left = 1;
    int right = 1;
    char leftChar = 0;
    char rightChar = 0;
    int window = 1;
};

class SegmentTree {
public:
    int n;
    string alp;
    vector<Node> tree;
    vector<int> indexes;

    SegmentTree(const string &s) {
        alp = s;
        n = (int)s.size();
        tree.resize(4 * n);
        indexes.resize(n);
        build(0, n - 1, 0);
    }

    void assignTreeIndex(int index, const Node &left, const Node &right) {
        Node &cur = tree[index];
        cur.leftChar = left.leftChar;
        cur.rightChar = right.rightChar;

        if (left.rightChar == right.leftChar) {
            int maxCnt = left.right + right.left;
            cur.maxLen = max({left.maxLen, right.maxLen, maxCnt});

            if (left.left == left.window)
                cur.left = maxCnt;
            else
                cur.left = left.left;

            if (right.right == right.window)
                cur.right = maxCnt;
            else
                cur.right = right.right;
        } else {
            cur.maxLen = max(left.maxLen, right.maxLen);
            cur.left = left.left;
            cur.right = right.right;
        }
    }

    Node build(int l, int r, int index) {
        if (l == r) {
            indexes[l] = index;
            tree[index].leftChar = alp[l];
            tree[index].rightChar = alp[l];
            tree[index].window = 1;
            tree[index].maxLen = 1;
            tree[index].left = 1;
            tree[index].right = 1;
            return tree[index];
        }

        int mid = (l + r) / 2;
        Node left = build(l, mid, index * 2 + 1);
        Node right = build(mid + 1, r, index * 2 + 2);

        tree[index].window = left.window + right.window;
        assignTreeIndex(index, left, right);

        return tree[index];
    }

    void update(int pos, char newVal) {
        int index = indexes[pos];
        tree[index].leftChar = newVal;
        tree[index].rightChar = newVal;
        tree[index].maxLen = 1;
        tree[index].left = 1;
        tree[index].right = 1;

        while (index > 0) {
            index = (index - 1) / 2;
            Node &left = tree[index * 2 + 1];
            Node &right = tree[index * 2 + 2];
            tree[index].window = left.window + right.window;
            assignTreeIndex(index, left, right);
        }
    }
};

class Solution {
public:
    vector<int> longestRepeating(string s, string queryCharacters, vector<int> &queryIndices) {
        int n = queryCharacters.size();
        SegmentTree segTree(s);
        vector<int> ret;
        ret.reserve(n);

        for (int i = 0; i < n; i++) {
            segTree.update(queryIndices[i], queryCharacters[i]);
            ret.push_back(segTree.tree[0].maxLen);
        }
        return ret;
    }
};
