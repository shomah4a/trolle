Ext.define('Trolle.model.User', {
    extend: 'Ext.data.Model',
    fields: [
        { name: 'text', type: 'string' },
        { name: 'iconCls',  type: 'string', defaultValue: 'user' },
        { name: 'leaf',  type: 'boolean', defaultValue: true }
    ]
});