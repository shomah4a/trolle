Ext.define('Trolle.model.Document', {
    extend: 'Ext.data.Model',

    fields: [
        { name: 'name', type: 'string' },
        { name: 'path', type: 'string' },
        { name: 'body', type: 'string' }
    ]
});