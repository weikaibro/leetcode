/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let target = []
    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) {
            target.push(arr[i])
        }
    }
    return target
};