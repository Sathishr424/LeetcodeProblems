// Last updated: 2/8/2025, 11:41:03 pm
#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int max_val = 0;
    int freq = 0;
};

class SegmentTree {
public:
    vector<Node> tree;
    vector<int> indexes;
    vector<int> index_to_compression;
    int n;

    SegmentTree(vector<int>& index_to_compression, int n) {
        this->index_to_compression = index_to_compression;
        this->n = n;
        tree.resize(n * 4);
        indexes.resize(n);
        build(0, n - 1, 0);
    }

    void build(int l, int r, int index) {
        if (l == r) {
            indexes[l] = index;
            tree[index].max_val = index_to_compression[l];
            return;
        }

        int mid = (l + r) / 2;
        build(l, mid, index * 2 + 1);
        build(mid + 1, r, index * 2 + 2);
    }

    void update(int index, int add) {
        index = indexes[index];
        tree[index].freq += add;

        while (index > 0) {
            index = (index - 1) / 2;
            int left = index * 2 + 1;
            int right = index * 2 + 2;

            if (tree[left].freq > tree[right].freq || 
                (tree[left].freq == tree[right].freq && tree[left].max_val < tree[right].max_val)) {
                tree[index].freq = tree[left].freq;
                tree[index].max_val = tree[left].max_val;
            } else {
                tree[index].freq = tree[right].freq;
                tree[index].max_val = tree[right].max_val;
            }
        }
    }
};

class Solution {
public:
    vector<int> subarrayMajority(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        int q_n = queries.size();
        int blockSize = sqrt(n) + 1;
        int m = (n + (blockSize - 1)) / blockSize;

        vector<vector<tuple<int, int, int, int>>> blocks(m);
        vector<tuple<int, int, int, int>> sorted_queries;

        for (int i = 0; i < q_n; ++i) {
            int l = queries[i][0], r = queries[i][1], t = queries[i][2];
            sorted_queries.emplace_back(l, r, t, i);
        }

        sort(sorted_queries.begin(), sorted_queries.end());

        int limit = blockSize - 1;
        int index = 0;
        vector<tuple<int, int, int, int>> currBlocks;

        for (auto& q : sorted_queries) {
            if (get<0>(q) > limit) {
                sort(currBlocks.begin(), currBlocks.end(), [](const auto& a, const auto& b) {
                    return get<1>(a) < get<1>(b);
                });
                blocks[index++] = currBlocks;
                currBlocks.clear();
                limit += blockSize;
            }
            currBlocks.push_back(q);
        }

        sort(currBlocks.begin(), currBlocks.end(), [](const auto& a, const auto& b) {
            return get<1>(a) < get<1>(b);
        });
        blocks[index] = currBlocks;

        vector<int> ret(q_n);
        map<int, int> compression;
        int c_index = 0;
        for (int num : nums) {
            if (compression.find(num) == compression.end()) {
                compression[num] = c_index++;
            }
        }

        vector<int> index_to_compression(c_index);
        for (auto& [num, idx] : compression) {
            index_to_compression[idx] = num;
        }

        SegmentTree tree(index_to_compression, c_index);

        int left = 0, right = -1;

        for (int block_id = 0; block_id < m; ++block_id) {
            for (auto& [l, r, t, i] : blocks[block_id]) {
                while (right < r) tree.update(compression[nums[++right]], 1);
                while (right > r) tree.update(compression[nums[right--]], -1);
                while (left < l) tree.update(compression[nums[left++]], -1);
                while (left > l) tree.update(compression[nums[--left]], 1);

                ret[i] = (tree.tree[0].freq >= t) ? tree.tree[0].max_val : -1;
            }
        }

        return ret;
    }
};
