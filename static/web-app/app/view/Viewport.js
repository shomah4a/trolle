Ext.define('Trolle.view.Viewport', {
    extend: 'Ext.container.Viewport',

    requires: [
        'Trolle.view.Toolbar',
        'Trolle.view.Outline',
        'Trolle.view.UserList',
        'Trolle.view.Log'
    ],

    layout: 'border',

    items: [
        {
            xtype: 'trolleToolbar',
            region: 'north'
        },
        {
            xtype: 'panel',
            region: 'west',
            width: 300,
            collapsible: true,
            split: true,

            layout: 'border',

            defaults: {
                split: true
            },

            items: [
                {
                    xtype: 'sourcetree',
                    region: 'north',
                    height: 300,
                    title: 'Tree'
                },
                {
                    xtype: 'outline',
                    region: 'center',
                    title: 'Outline'
                }
            ]
        },
        {
            xtype: 'tabpanel',

            itemId: 'document-tab-panel',

            region: 'center',

            defaults: {
                xtype: 'documentpanel',
                closable: true
            }
        },
        {
            xtype: 'panel',
            region: 'east',
            width: 300,
            collapsible: true,
            split: true,

            layout: 'border',

            defaults: {
                split: true
            },

            items: [
                {
                    xtype: 'userlist',
                    region: 'north',
                    height: 300,
                    title: 'User'
                },
                {
                    xtype: 'log',
                    region: 'center',
                    title: 'Log'
                }
            ]
        }
    ]
});