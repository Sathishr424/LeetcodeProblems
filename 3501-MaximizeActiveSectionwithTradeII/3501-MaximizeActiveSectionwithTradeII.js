// Last updated: 17/6/2025, 12:14:35 am
const cmax = (x, y) => x > y ? x : y;
const cmin = (x, y) => x < y ? x : y;

class Node {
    constructor(n) {
        this.LF = n;
        this.LS = n;
        this.RF = -1;
        this.RS = -1;
        this.val = 0;
        this.l = n;
        this.r = -1;
    }
}

function maxActiveSectionsAfterTrade(s, queries) {
    const n = s.length;
    let total = 0;
    for (let i = 0; i < n; i++) {
        total += s[i] === '1';
    }

    const zeros_left = Array(n).fill(0);
    const zeros_right = Array(n).fill(0);

    let i = 0;
    while (i < n) {
        if (s[i] === '0') {
            let j = i;
            while (j < n && s[j] === '0') {
                zeros_left[j] = i;
                j++;
            }
            i = j;
        } else {
            i++;
        }
    }

    i = n - 1;
    while (i >= 0) {
        if (s[i] === '0') {
            let j = i;
            while (j >= 0 && s[j] === '0') {
                zeros_right[j] = i;
                j--;
            }
            i = j;
        } else {
            i--;
        }
    }

    const tree = Array(n * 4).fill(null);

    function calcIntersection(left, right, l, r, mid) {
        const ls = right.LS;
        const rf = left.RF;
        let ans = 0;

        if (ls !== n && rf !== -1) {
            let curr = 0;
            curr += rf - cmax(zeros_left[rf], l) + 1;
            curr += zeros_right[rf] - rf;
            curr += cmin(zeros_right[ls], r) - ls + 1;
            ans = cmax(ans, curr);
        }

        const rs = left.RS;
        const lf = right.LF;

        if (rs !== -1 && lf !== n) {
            let curr = 0;
            curr += lf - zeros_left[lf] + 1;
            curr += cmin(r, zeros_right[lf]) - lf;
            curr += rs - cmax(zeros_left[rs], l) + 1;
            ans = cmax(ans, curr);
        }

        if (s[mid] === '1' && s[mid + 1] === '1') {
            let curr = 0;
            const rs = left.RS;
            const ls = right.LS;
            if (rs !== -1 && ls !== n) {
                curr += rs - cmax(zeros_left[rs], l) + 1;
                curr += cmin(zeros_right[ls], r) - ls + 1;
                ans = cmax(ans, curr);
            }
        }

        return ans;
    }

    function calcNode(left, right) {
        const l = left.l;
        const r = right.r;
        const mid = left.r;

        const node = new Node(n);
        node.l = l;
        node.r = r;

        node.LF = left.LF;
        node.RF = right.RF;

        if (s[mid] === '1') {
            node.LS = cmin(left.LS, cmin(right.LF, right.LS));
        } else {
            node.LS = cmin(left.LS, right.LS);
        }

        if (s[mid + 1] === '1') {
            node.RS = cmax(right.RS, cmax(left.RF, left.RS));
        } else {
            node.RS = cmax(right.RS, left.RS);
        }

        node.val = cmax(cmax(left.val, right.val), calcIntersection(left, right, l, r, mid));
        return node;
    }

    function buildTree(l, r, index) {
        if (l === r) {
            tree[index] = new Node(n);
            if (s[l] === '0') {
                tree[index].LF = l;
                tree[index].RF = l;
            }
            tree[index].l = l;
            tree[index].r = l;
            return;
        }

        const mid = Math.floor((l + r) / 2);
        buildTree(l, mid, index * 2 + 1);
        buildTree(mid + 1, r, index * 2 + 2);

        const left = tree[index * 2 + 1];
        const right = tree[index * 2 + 2];
        tree[index] = calcNode(left, right);
    }

    function query(l, r, index, left, right) {
        if (l > right || r < left) return null;
        if (l >= left && r <= right) return tree[index];

        const mid = Math.floor((l + r) / 2);
        const left_ans = query(l, mid, index * 2 + 1, left, right);
        const right_ans = query(mid + 1, r, index * 2 + 2, left, right);

        if (left_ans && right_ans) return calcNode(left_ans, right_ans);
        if (left_ans) return left_ans;
        return right_ans;
    }

    buildTree(0, n - 1, 0);

    const trades = [];
    for (const [l, r] of queries) {
        const ans = query(0, n - 1, 0, l, r);
        trades.push((ans ? ans.val : 0) + total);
    }

    return trades;
}
