Ext.define('Trolle.store.Document', {
    extend: 'Ext.data.Store',
    requires: [
        'Trolle.model.Document'
    ],

    model: 'Trolle.model.Document',

    autoLoad: true,

    proxy: {
        type: 'ajax',
        url: 'data/document.json',
        reader: {
            type: 'json'
        }
    }
});