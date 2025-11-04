/**
 * @param {number} n
 * @return {boolean}
 */
/* var isPowerOfTwo = function(n) {
    if(n==0) return false
    if(n==1) return true
    if(n<0) return false
    return Number.isInteger(Math.log2(n)) ? true : false
}; */

var isPowerOfTwo = function (n) {
    if (n == 0) return false
    if (n == 1) return true
    if (n < 0) return false
    if (n % 2 == 0) return false
    n = isPowerOfTwo(n/2)
    return n == 1
};