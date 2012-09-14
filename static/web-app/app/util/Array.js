/**
 * @class Trolle.util.Array
 */
Ext.define('Trolle.util.Array', {
    singleton: true,

    /**
     * Creates a new array with the results except null of calling a provided function on every element in this array.
     * @param {Array} array
     * @param {Function} fn Callback function for each item
     * @param {Object} scope Callback function scope
     * @return {Array} results
     */
    collect: function(array, fn, scope) {
        var results = [],
            r,
            i = 0,
            index = 0,
            len = array.length;

        for (; i < len; i++) {
            r = fn.call(scope, array[i], i, array);
            if (r !== null) {
                results[index] = r;
                index++;
            }
        }

        return results;
    },

    /**
     * takes a function and a array and returns the first element in the array matching the function, or defalutValue if there is no such element.
     * @param {Array} array
     * @param {Function} fn Callback function for each item
     * @param {Object} scope Callback function scope
     * @param {Object=} defalutValue if there is no such element, return this value
     * @return {Object} result
     */
    find: function(array, fn, scope, defaultValue) {
        defaultValue = defaultValue || null;

        var result,
            i = 0,
            index = 0,
            len = array.length;

        for (; i < len; i++) {
            if (fn.call(scope, array[i], i, array)) {
                return array[i];
            }
        }

        return defaultValue;
    }
});
