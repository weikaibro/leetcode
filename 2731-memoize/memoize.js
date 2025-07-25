/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    memo = {}
    return function(...args) {
        if (memo[args] !== undefined) {
            return memo[args]
        } else {
            memo[args] = fn(...args)
            return memo[args]
        }
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */