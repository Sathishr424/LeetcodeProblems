// Last updated: 24/8/2025, 7:10:53 pm
class SegmentTree {
public:
    int n;
    vector<int> tree;
    vector<int> indexes;

    SegmentTree(int n_) {
        n = n_;
        tree.assign(4 * n, 0);
        indexes.assign(n, 0);
        build(0, n - 1, 0);
    }

    void build(int l, int r, int index) {
        if (l == r) {
            indexes[l] = index;
            return;
        }
        int mid = (l + r) / 2;
        build(l, mid, index * 2 + 1);
        build(mid + 1, r, index * 2 + 2);
    }

    int query(int l, int r, int index, int left, int right) {
        if (l > right || r < left) return 0;
        if (l >= left && r <= right) return tree[index];
        int mid = (l + r) / 2;
        return max(query(l, mid, index * 2 + 1, left, right),
                   query(mid + 1, r, index * 2 + 2, left, right));
    }

    void update(int idx, int new_val) {
        int index = indexes[idx];
        tree[index] = new_val;
        while (index > 0) {
            index = (index - 1) / 2;
            tree[index] = max(tree[index * 2 + 1], tree[index * 2 + 2]);
        }
    }
};

class Solution {
public:
    vector<int> maxValue(vector<int>& nums) {
        int n = nums.size();

        vector<int> left(n);
        left[0] = nums[0];
        int maxi = nums[0];
        for (int i = 1; i < n; i++) {
            maxi = max(maxi, nums[i]);
            left[i] = maxi;
        }

        map<int, int> compressed;
        int index = 0;
        vector<int> sorted_nums = nums;
        sort(sorted_nums.begin(), sorted_nums.end());
        for (int num : sorted_nums) {
            if (compressed.find(num) == compressed.end()) {
                compressed[num] = index++;
            }
        }

        SegmentTree tree(index);
        vector<int> ret(n, 0);

        for (int i = n - 1; i >= 0; i--) {
            int el = tree.query(0, index - 1, 0, 0, max(compressed[left[i]], compressed[nums[i]]) - 1);

            ret[i] = max(el, left[i]);
            tree.update(compressed[nums[i]], ret[i]);
        }

        return ret;
    }
};
