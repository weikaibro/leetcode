/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    return this.reduce((acc, curr) => {
        const arr_key = fn(curr)
        if (!acc[arr_key]) {
            acc[arr_key] = []
        }
        acc[arr_key].push(curr)
        return acc
    }, {})
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */