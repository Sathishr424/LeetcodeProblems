// Last updated: 11/11/2025, 12:42:01 am
#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;

void print1DVector(vector<int> v) {
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
    cout << endl;
}

class SegmentTree {
    public:
    SegmentTree(int n) {
        this->n = n;
        tree.assign(n * 4, 0);
    }

    int update(int l, int r, int index, int update_index) {
        if (l == r) {
            tree[index] += 1;
            return tree[index];
        }

        int mid = (l + r) / 2;
        if (update_index <= mid) {
            tree[index] = update(l, mid, index * 2 + 1, update_index) + tree[index * 2 + 2];
        } else {
            tree[index] = update(mid + 1, r, index * 2 + 2, update_index) + tree[index * 2 + 1];
        }
        return tree[index];
    }

    int query(int l, int r, int index, int right_index) {
        // cout << l << " " << r << " " << right_index << " " << tree[index] << endl;
        if (l > right_index) return 0;

        if (r <= right_index) {
            return tree[index];
        }

        int mid = (l + r) / 2;

        return query(l, mid, index * 2 + 1, right_index) + query(mid + 1, r, index * 2 + 2, right_index);
    }

    vector<int> getTree() {
        return tree;
    }

private:
    int n;
    vector<int> tree;
};

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        // print1DVector(nums);
        int n = nums.size();

        std::vector<int> sorted_nums = nums;
        unordered_map<int, int> path_compression;
        int index = 0;

        sort(sorted_nums.begin(), sorted_nums.end());
        for (int num: sorted_nums) {
            if (path_compression.find(num) == path_compression.end()) {
                path_compression[num] = index;
                index++;
            }
        }
        int m = path_compression.size();
        SegmentTree tree(m);
        vector<int> ans(n, 0);
        for (int i=n-1; i>=0; i--) {
            ans[i] = tree.query(0, m-1, 0, path_compression[nums[i]] - 1);
            tree.update(0, m-1, 0, path_compression[nums[i]]);
            // cout << nums[i] << " " << path_compression[nums[i]] << endl;
            // print1DVector(tree.getTree());
        }

        return ans;
    }
};