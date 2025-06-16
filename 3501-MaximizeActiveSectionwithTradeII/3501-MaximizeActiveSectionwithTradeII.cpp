// Last updated: 17/6/2025, 12:58:11 am
#include <bits/stdc++.h>
using namespace std;

#define cmax(a, b) ((a) > (b) ? (a) : (b))
#define cmin(a, b) ((a) < (b) ? (a) : (b))

struct Node {
    int LF, LS, RF, RS, val, l, r;
    Node(int n) {
        LF = LS = n;
        RF = RS = -1;
        val = 0;
        l = n;
        r = -1;
    }
};

class Solution {
public:
    vector<Node> tree;
    string s;
    vector<int> zeros_left, zeros_right;
    int n;

    int calcIntersection(Node &left, Node &right, int l, int r, int mid) {
        int ls = right.LS;
        int rf = left.RF;

        int ans = 0;
        if (ls != n && rf != -1) {
            int curr = 0;
            curr += rf - cmax(zeros_left[rf], l) + 1;
            curr += zeros_right[rf] - rf;
            curr += cmin(zeros_right[ls], r) - ls + 1;
            ans = cmax(ans, curr);
        }

        int rs = left.RS;
        int lf = right.LF;

        if (rs != -1 && lf != n) {
            int curr = 0;
            curr += lf - zeros_left[lf] + 1;
            curr += cmin(r, zeros_right[lf]) - lf;
            curr += rs - cmax(zeros_left[rs], l) + 1;
            ans = cmax(ans, curr);
        }

        if (s[mid] == '1' && s[mid + 1] == '1') {
            int curr = 0;
            rs = left.RS;
            ls = right.LS;

            if (rs != -1 && ls != n) {
                curr += rs - cmax(zeros_left[rs], l) + 1;
                curr += cmin(zeros_right[ls], r) - ls + 1;
                ans = cmax(ans, curr);
            }
        }

        return ans;
    }

    Node calcNode(Node &left, Node &right) {
        int l = left.l;
        int r = right.r;
        int mid = left.r;

        Node node(n);
        node.l = l;
        node.r = r;

        node.LF = left.LF;
        node.RF = right.RF;

        if (s[mid] == '1')
            node.LS = cmin(left.LS, cmin(right.LF, right.LS));
        else
            node.LS = cmin(left.LS, right.LS);

        if (s[mid + 1] == '1')
            node.RS = cmax(right.RS, cmax(left.RF, left.RS));
        else
            node.RS = cmax(right.RS, left.RS);

        node.val = cmax(cmax(left.val, right.val), calcIntersection(left, right, l, r, mid));

        return node;
    }

    void buildTree(int l, int r, int index) {
        if (l == r) {
            tree[index] = Node(n);
            if (s[l] == '0')
                tree[index].LF = tree[index].RF = l;
            tree[index].l = l;
            tree[index].r = l;
            return;
        }

        int mid = (l + r) / 2;
        buildTree(l, mid, 2 * index + 1);
        buildTree(mid + 1, r, 2 * index + 2);

        tree[index] = calcNode(tree[2 * index + 1], tree[2 * index + 2]);
    }

    Node query(int l, int r, int index, int left, int right) {
        if (l > right || r < left)
            return Node(n);

        if (l >= left && r <= right)
            return tree[index];

        int mid = (l + r) / 2;
        Node left_ans = query(l, mid, 2 * index + 1, left, right);
        Node right_ans = query(mid + 1, r, 2 * index + 2, left, right);

        if (left_ans.l != n && right_ans.l != n)
            return calcNode(left_ans, right_ans);
        else if (left_ans.l != n)
            return left_ans;
        else
            return right_ans;
    }

    vector<int> maxActiveSectionsAfterTrade(string str, vector<vector<int>> &queries) {
        s = str;
        n = s.length();

        zeros_left.assign(n, 0);
        zeros_right.assign(n, 0);
        tree.assign(n * 4, Node(n));

        int total = count(s.begin(), s.end(), '1');

        for (int i = 0; i < n; ) {
            if (s[i] == '0') {
                int j = i;
                while (j < n && s[j] == '0') {
                    zeros_left[j] = i;
                    j++;
                }
                i = j;
            } else i++;
        }

        for (int i = n - 1; i >= 0; ) {
            if (s[i] == '0') {
                int j = i;
                while (j >= 0 && s[j] == '0') {
                    zeros_right[j] = i;
                    j--;
                }
                i = j;
            } else i--;
        }

        buildTree(0, n - 1, 0);
        vector<int> res;

        for (auto &q : queries) {
            int l = q[0], r = q[1];
            Node ans = query(0, n - 1, 0, l, r);
            res.push_back(ans.val + total);
        }

        return res;
    }
};
