/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
    this.obj = nums
    console.log(this.obj)
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    return this.obj.reduce((acc, curr) => {
        return acc + curr
    }, 0)
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    return "[" + this.obj + "]"
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */