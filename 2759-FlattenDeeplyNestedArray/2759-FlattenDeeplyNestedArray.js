// Last updated: 12/6/2025, 5:37:00 am
/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n, ret=[]) {
    if (n == 0){
        for (let x of arr){
            ret.push(x);
        }
        return ret;
    }
    for (let i=0; i<arr.length; i++){
        if (typeof arr[i] === 'number'){
            ret.push(arr[i]);
        }else{
            flat(arr[i], n-1, ret);
        }
    }
    return ret;
};