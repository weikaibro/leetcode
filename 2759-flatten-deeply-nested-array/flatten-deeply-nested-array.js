/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    for (let i = 0; i < n; i++) {
        let temp = []
        let isFlat = true
        for (let j = 0; j < arr.length; j++) {
            if (Array.isArray(arr[j])) {
                for (let z = 0; z < arr[j].length; z++) {
                    temp.push(arr[j][z])
                    isFlat = false
                }
            } else {
                temp.push(arr[j])
            }
        }
        arr = temp
        if (isFlat) break
    }
    return arr
};