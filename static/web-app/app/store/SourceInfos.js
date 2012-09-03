Ext.define('Trolle.store.SourceInfos', {
    extend: 'Ext.data.TreeStore',
    requires: [
        'Trolle.model.SourceInfo'
    ],

    model: 'Trolle.model.SourceInfo',

    proxy: {
        type: 'ajax',
        url: 'data/sourceInfos.json',
        reader: 'json'
    },

    listeners: {
        append: function(thisNode, newChildNode, index, eOpts) {
            newChildNode.set('text', newChildNode.get('name'));
        }
    },

});