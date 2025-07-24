/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let result = []
    let start = 0
    while (start < arr.length) {
        let group = []
        for (let i = start; i < Math.min(start + size, arr.length); i++) {
            group.push(arr[i])
        }
        result.push(group)
        start += size
    }
    return result
};
