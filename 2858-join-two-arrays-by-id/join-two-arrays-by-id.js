/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    obj = {}
    for (let i = 0; i < arr1.length; i++) {
        obj[arr1[i].id] = arr1[i]
        // console.log(obj)
        // { '1': { id: 1, x: 2, y: 3 } }
        // { '1': { id: 1, x: 2, y: 3 }, '2': { id: 2, x: 3, y: 6 } }
    } 
    for (let i = 0; i < arr2.length; i++) {
        if (obj[arr2[i].id]) {
            for (const key in arr2[i]) {
                obj[arr2[i].id][key] = arr2[i][key] 
            }
        } else {
            obj[arr2[i].id] = arr2[i]
        }
    }
    return Object.values(obj)
};