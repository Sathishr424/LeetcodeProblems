// Last updated: 19/6/2025, 12:21:21 am
const int N = 1e9;

class SegNode {
public:
    int l, r;
    bool track;
    int lazy;
    SegNode* left;
    SegNode* right;

    SegNode(int _l, int _r) {
        l = _l;
        r = _r;
        track = false;
        lazy = -1;
        left = nullptr;
        right = nullptr;
    }
};

class SegTree {
public:
    SegNode* root;

    SegTree() {
        root = new SegNode(0, N);
    }

    void push(SegNode* node) {
        int mid = (node->l + node->r) / 2;
        if (!node->left)
            node->left = new SegNode(node->l, mid);
        if (!node->right)
            node->right = new SegNode(mid + 1, node->r);

        if (node->lazy != -1) {
            bool val = (node->lazy == 1);
            node->left->track = val;
            node->right->track = val;
            node->left->lazy = node->lazy;
            node->right->lazy = node->lazy;
            node->lazy = -1;
        }
    }

    void add(SegNode* node, int s, int e) {
        if (node->r < s || node->l > e) return;
        if (node->l >= s && node->r <= e) {
            node->track = true;
            node->lazy = 1;
            return;
        }

        push(node);
        add(node->left, s, e);
        add(node->right, s, e);

        node->track = node->left->track && node->right->track;
    }

    void remove(SegNode* node, int s, int e) {
        if (node->r < s || node->l > e) return;
        if (node->l >= s && node->r <= e) {
            node->track = false;
            node->lazy = 0;
            return;
        }

        push(node);
        remove(node->left, s, e);
        remove(node->right, s, e);

        node->track = node->left->track && node->right->track;
    }

    bool query(SegNode* node, int s, int e) {
        if (node->r < s || node->l > e) return true;
        if (node->l >= s && node->r <= e) return node->track;

        push(node);
        return query(node->left, s, e) && query(node->right, s, e);
    }
};

class RangeModule {
private:
    SegTree tree;

public:
    RangeModule() {}

    void addRange(int left, int right) {
        tree.add(tree.root, left, right - 1);
    }

    bool queryRange(int left, int right) {
        return tree.query(tree.root, left, right - 1);
    }

    void removeRange(int left, int right) {
        tree.remove(tree.root, left, right - 1);
    }
};
