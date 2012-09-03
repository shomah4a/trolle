Ext.define('Trolle.view.Log', {
    extend: 'Ext.grid.Panel',

    alias: 'widget.log',

    store: 'Logs',

    emptyText: 'No Logs',
    columns: {
        items: [
            {
                text: 'User',
                dataIndex: 'user',
                flex: 3
            },
            {
                text: 'Msg',
                flex: 7,
                renderer: function() {
                    return '';
                }
            }
        ],
    }

});