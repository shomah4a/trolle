/**
 * @class Trolle.util.Array
 */
Ext.define('Trolle.util.Object', {
    singleton: true,

    map: function(object, fn, scope) {
        var result = [];
        for (var property in object) {
            if (object.hasOwnProperty(property)) {
                result.push(fn.call(scope || object, property, object[property], object));
            }
        }
        return result;
    }
});