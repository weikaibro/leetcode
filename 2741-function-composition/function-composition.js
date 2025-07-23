/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    
    return function(x) {
        for (let i = functions.length - 1; i >= 0; i--) {
            let fn = functions[i]
            x = fn(x)
        }
        return x
        // while (functions.length) {
        //     let fn = functions.pop()
        //     x = fn(x)
        // }
        // return x
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */