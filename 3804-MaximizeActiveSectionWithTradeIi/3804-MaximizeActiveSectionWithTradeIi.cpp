// Last updated: 12/25/2025, 7:12:00 PM
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int left = 0, right = 0, maxVal = 0;
    Node() {}
    Node(int l, int r, int m) : left(l), right(r), maxVal(m) {}
};

int cmax(int x, int y) { return x > y ? x : y; }
int cmin(int x, int y) { return x < y ? x : y; }

class Solution {
public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        int n = s.size();
        int total_ones = count(s.begin(), s.end(), '1');
        int k = floor(log2(n)) + 1;
        vector<vector<Node>> s_table(k, vector<Node>(n));

        vector<int> zero_prefix(n + 1, 0);
        for (int i = 0; i < n; i++) {
            zero_prefix[i + 1] = zero_prefix[i] + (s[i] == '0');
        }

        vector<int> zeros_left(n, -1), zeros_right(n, -1);
        char prev = s[0];
        int index = -1;
        for (int i = 1; i < n; i++) {
            if (prev != s[i]) {
                if (prev == '0') index = i - 1;
                prev = s[i];
            }
            zeros_left[i] = index;
        }

        prev = s[n - 1];
        index = -1;
        for (int i = n - 2; i >= 0; i--) {
            if (prev != s[i]) {
                if (prev == '0') index = i + 1;
                prev = s[i];
            }
            zeros_right[i] = index;
        }

        vector<int> zero_prefix_left(n, 0), zero_prefix_right(n, n - 1);
        prev = s[0];
        int prev_index = 0;
        for (int i = 1; i < n; i++) {
            if (prev != s[i]) {
                prev = s[i];
                prev_index = i;
            }
            if (s[i] == '0') zero_prefix_left[i] = prev_index;
        }

        prev = s[n - 1];
        prev_index = n - 1;
        for (int i = n - 2; i >= 0; i--) {
            if (prev != s[i]) {
                prev = s[i];
                prev_index = i;
            }
            if (s[i] == '0') zero_prefix_right[i] = prev_index;
        }

        for (int i = 0; i < n; i++) {
            if (s[i] == '0') {
                s_table[0][i].left = 0;
                s_table[0][i].right = 0;
            } else {
                s_table[0][i].left = 1;
                s_table[0][i].right = 1;
            }
        }

        auto getMaxNode = [&](int l, int mid, int r, Node& left, Node& right) {
            Node node;
            node.left = left.left;
            node.right = right.right;

            int curr = cmax(left.maxVal, right.maxVal);

            if (left.right == 0) {
                if (right.left == 0) {
                    int left_index = zeros_left[mid];
                    if (left_index != -1 && left_index >= l) {
                        left_index = cmax(l, zero_prefix_left[left_index]);
                        int right_index = cmin(r, zero_prefix_right[mid + 1]);
                        curr = cmax(curr, zero_prefix[right_index + 1] - zero_prefix[left_index]);
                    }
                }
                int left_index = cmax(l, zero_prefix_left[mid]);
                int right_index = zeros_right[mid + 1];
                if (right_index != -1 && right_index <= r) {
                    right_index = cmin(r, zero_prefix_right[right_index]);
                    curr = cmax(curr, zero_prefix[right_index + 1] - zero_prefix[left_index]);
                }
            } else {
                int left_index = zeros_left[mid];
                if (left_index != -1 && left_index >= l) {
                    left_index = cmax(l, zero_prefix_left[left_index]);
                    if (right.left == 1) {
                        int right_index = zeros_right[mid + 1];
                        if (right_index != -1 && right_index <= r) {
                            right_index = cmin(r, zero_prefix_right[right_index]);
                            curr = cmax(curr, zero_prefix[right_index + 1] - zero_prefix[left_index]);
                        }
                    } else {
                        int right_index = cmin(r, zero_prefix_right[mid + 1]);
                        curr = cmax(curr, zero_prefix[right_index + 1] - zero_prefix[left_index]);
                    }
                }
            }

            node.maxVal = curr;
            return node;
        };

        for (int power = 1; power < k; power++) {
            int m = 1 << power;
            int prev_m = m >> 1;
            for (int i = 0; i + m <= n; i++) {
                s_table[power][i] = getMaxNode(i, i + prev_m - 1, i + m - 1, s_table[power - 1][i], s_table[power - 1][i + prev_m]);
            }
        }

        vector<int> ret;
        for (auto& q : queries) {
            int l = q[0], r = q[1];
            int dis = r - l + 1;
            int power = 0;
            Node* prev = nullptr;
            int x = l;
            while (dis) {
                if (dis & 1) {
                    Node curr = s_table[power][l];
                    int mid = l - 1;
                    l += 1 << power;
                    if (prev != nullptr) {
                        Node combined = getMaxNode(x, mid, l - 1, *prev, curr);
                        *prev = combined;
                    } else {
                        prev = new Node(curr);
                    }
                }
                dis >>= 1;
                power++;
            }
            ret.push_back(prev->maxVal + total_ones);
            delete prev;
        }
        return ret;
    }
};
