/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let obj = {}
    return function(...args) {
        const timer = setTimeout(() => fn(...args), t)
        if (fn in obj) {
            clearTimeout(obj[fn])
        }
        obj[fn] = timer
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */