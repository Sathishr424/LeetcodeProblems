// Last updated: 9/7/2025, 11:36:36 pm
const cmax = (x, y) => x > y ? x : y;
const cmin = (x, y) => x < y ? x : y;

class Node {
    constructor() {
        this.left = 0;
        this.right = 0;
        this.max = 0;
    }

    toString() {
        return `(${this.left}, ${this.right}, ${this.max})`;
    }
}

function maxActiveSectionsAfterTrade(s, queries) {
    const n = s.length;
    const total_ones = [...s].filter(c => c === '1').length;
    const k = Math.floor(Math.log2(n)) + 1;
    const s_table = Array.from({ length: k }, () => Array.from({ length: n }, () => new Node()));

    const zero_prefix = [0];
    for (let i = 0; i < n; i++) {
        zero_prefix.push(zero_prefix[zero_prefix.length - 1] + (s[i] === '0' ? 1 : 0));
    }

    const zeros_left = Array(n).fill(-1);
    let prev = s[0];
    let index = -1;

    for (let i = 1; i < n; i++) {
        if (prev !== s[i]) {
            if (prev === '0') {
                index = i - 1;
            }
            prev = s[i];
        }
        zeros_left[i] = index;
    }

    const zeros_right = Array(n).fill(-1);
    prev = s[n - 1];
    index = -1;

    for (let i = n - 2; i >= 0; i--) {
        if (prev !== s[i]) {
            if (prev === '0') {
                index = i + 1;
            }
            prev = s[i];
        }
        zeros_right[i] = index;
    }

    const zero_prefix_left = Array(n).fill(0);
    const zero_prefix_right = Array(n).fill(n - 1);

    prev = s[0];
    let prev_index = 0;
    for (let i = 1; i < n; i++) {
        if (prev !== s[i]) {
            prev = s[i];
            prev_index = i;
        }
        if (s[i] === '0') {
            zero_prefix_left[i] = prev_index;
        }
    }

    prev = s[n - 1];
    prev_index = n - 1;
    for (let i = n - 2; i >= 0; i--) {
        if (prev !== s[i]) {
            prev = s[i];
            prev_index = i;
        }
        if (s[i] === '0') {
            zero_prefix_right[i] = prev_index;
        }
    }

    for (let i = 0; i < n; i++) {
        if (s[i] === '0') {
            s_table[0][i].left = 0;
            s_table[0][i].right = 0;
        } else {
            s_table[0][i].left = 1;
            s_table[0][i].right = 1;
        }
    }

    function getMaxNode(l, mid, r, left, right) {
        const node = new Node();
        node.left = left.left;
        node.right = right.right;

        let curr = cmax(left.max, right.max);

        if (left.right === 0) {
            if (right.left === 0) {
                let left_index = zeros_left[mid];
                if (left_index !== -1 && left_index >= l) {
                    left_index = cmax(l, zero_prefix_left[left_index]);
                    let right_index = cmin(r, zero_prefix_right[mid + 1]);
                    curr = cmax(curr, zero_prefix[right_index + 1] - zero_prefix[left_index]);
                }
            }
            let left_index = cmax(l, zero_prefix_left[mid]);
            let right_index = zeros_right[mid + 1];
            if (right_index !== -1 && right_index <= r) {
                right_index = cmin(r, zero_prefix_right[right_index]);
                curr = cmax(curr, zero_prefix[right_index + 1] - zero_prefix[left_index]);
            }
        } else {
            let left_index = zeros_left[mid];
            if (left_index !== -1 && left_index >= l) {
                left_index = cmax(l, zero_prefix_left[left_index]);

                if (right.left === 1) {
                    let right_index = zeros_right[mid + 1];
                    if (right_index !== -1 && right_index <= r) {
                        right_index = cmin(r, zero_prefix_right[right_index]);
                        curr = cmax(curr, zero_prefix[right_index + 1] - zero_prefix[left_index]);
                    }
                } else {
                    let right_index = cmin(r, zero_prefix_right[mid + 1]);
                    curr = cmax(curr, zero_prefix[right_index + 1] - zero_prefix[left_index]);
                }
            }
        }

        node.max = curr;
        return node;
    }

    for (let power = 1; power < k; power++) {
        let m = 1 << power;
        let prev_m = m >> 1;
        for (let i = 0; i <= n - m; i++) {
            const left = s_table[power - 1][i];
            const right = s_table[power - 1][i + prev_m];
            s_table[power][i] = getMaxNode(i, i + prev_m - 1, i + m - 1, left, right);
        }
    }

    const ret = [];
    for (const [ql, qr] of queries) {
        let l = ql;
        let dis = qr - ql + 1;
        let power = 0;
        let prev = null;
        let x = l;

        while (dis) {
            if (dis & 1) {
                const curr = s_table[power][l];
                const mid = l - 1;
                l += 1 << power;
                if (prev !== null) {
                    prev = getMaxNode(x, mid, l - 1, prev, curr);
                } else {
                    prev = curr;
                }
            }
            dis >>= 1;
            power++;
        }

        ret.push(prev.max + total_ones);
    }

    return ret;
}