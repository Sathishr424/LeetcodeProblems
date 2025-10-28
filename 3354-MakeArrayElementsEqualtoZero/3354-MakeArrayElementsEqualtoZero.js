// Last updated: 28/10/2025, 2:03:41 pm
var countValidSelections = function(nums) {
    const n = nums.length;
    let cnt = 0;

    function isValid(index, d, arr) {
        if (index === n || index === -1) {
            for (let num of arr) {
                if (num !== 0) return 0;
            }
            return 1;
        }

        if (arr[index] === 0) {
            return isValid(index + d, d, arr);
        } else {
            arr[index] -= 1;
            d = d - (2 * d);
            return isValid(index + d, d, arr);
        }
    }

    for (let i = 0; i < n; i++) {
        if (nums[i] === 0) {
            cnt += isValid(i, 1, nums.slice()) + isValid(i, -1, nums.slice());
        }
    }

    return cnt;
};