Ext.define('Trolle.store.Logs', {
    extend: 'Ext.data.Store',
    requires: [
        'Trolle.model.Log'
    ],

    model: 'Trolle.model.Log',

    autoLoad: true,

    proxy: {
        type: 'ajax',
        url: 'data/logs.json',
        reader: {
            type: 'json',
            root: 'data'
        }
    }
});