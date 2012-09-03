Ext.define('Trolle.store.Users', {
    extend: 'Ext.data.TreeStore',
    requires: [
        'Trolle.model.User'
    ],

    model: 'Trolle.model.User',

    proxy: {
        type: 'ajax',
        url: 'data/users.json',
        reader: 'json'
    }
});