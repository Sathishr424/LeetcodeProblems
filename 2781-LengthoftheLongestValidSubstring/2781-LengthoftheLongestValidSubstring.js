// Last updated: 29/7/2025, 11:05:19 pm
function longestValidSubstring(word, forbidden) {
    const n = word.length;
    const remove = new Set(forbidden);

    const dp = Array.from({ length: n }, () => Array(10).fill(0));

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < 10; j++) {
            if (i + j + 1 <= n && remove.has(word.substring(i, i + j + 1))) {
                dp[i][j] = 1;
            }
        }
    }

    const k = Math.floor(Math.log2(n)) + 1;
    const logs = Array.from({ length: k }, () => Array(n).fill(true));

    for (let i = 0; i < n; i++) {
        logs[0][i] = !remove.has(word[i]);
    }

    for (let power = 1; power < k; power++) {
        const m = 1 << power;
        const prev_m = m >> 1;
        for (let i = 0; i + m <= n; i++) {
            logs[power][i] = logs[power - 1][i] && logs[power - 1][i + prev_m];
            if (!logs[power][i]) continue;

            const index = i + prev_m;
            const l = Math.max(i, index - 10);
            const r = Math.min(i + m, index + 10);
            for (let j = l; j < index; j++) {
                for (let k = index; k < r; k++) {
                    if (k - j >= 10) break;
                    if (dp[j][k - j]) {
                        logs[power][i] = false;
                        break;
                    }
                }
                if (!logs[power][i]) break;
            }
        }
    }

    function isGood(dis) {
        const power = Math.floor(Math.log2(dis));
        const half_power = 1 << power;
        for (let i = 0; i + dis <= n; i++) {
            const index = i + dis - half_power;
            if (logs[power][i] && logs[power][index]) {
                let match = true;
                const l = Math.max(i, index - 10);
                const r = Math.min(i + dis, index + 10);
                for (let j = l; j < index; j++) {
                    for (let k = index; k < r; k++) {
                        if (k - j >= 10) break;
                        if (dp[j][k - j]) {
                            match = false;
                            break;
                        }
                    }
                    if (!match) break;
                }
                if (match) return true;
            }
        }
        return false;
    }

    let l = 0, r = n;
    while (l < r) {
        const mid = Math.floor((l + r + 1) / 2);
        if (isGood(mid)) {
            l = mid;
        } else {
            r = mid - 1;
        }
    }

    return l;
}
