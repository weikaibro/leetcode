/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let OnceCall = true
    // use closure to store previous state
    return function(...args) {
        if (OnceCall) {
            OnceCall = false
            return fn(...args)
        } else {
            return undefined
        }
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
