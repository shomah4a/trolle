Ext.define('Trolle.store.Outlines', {
    extend: 'Ext.data.TreeStore',
    requires: [
        'Trolle.model.Outline'
    ],

    model: 'Trolle.model.Outline',

    proxy: {
        type: 'ajax',
        url: 'data/outlines.json',
        reader: 'json'
    },

    listeners: {
        append: function(thisNode, newChildNode, index, eOpts) {
            newChildNode.set('text', newChildNode.get('name'));
            newChildNode.set('leaf', Ext.isEmpty(newChildNode.get('children')));
            newChildNode.set('iconCls', 'outline-function');

        }
    },

});