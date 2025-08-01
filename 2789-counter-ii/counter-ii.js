/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    initialVal = init
    return {
        increment: () => {
            return ++init
        },
        reset: () => {
            init = initialVal
            return init
        },
        decrement: () => {
            return --init
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */