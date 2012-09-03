/**
 * @class Trolle.view.Toolbar
 * @extends Ext.toolbar.Toolbar
 */
Ext.define('Trolle.view.Toolbar', {
    extend: 'Ext.toolbar.Toolbar',
    alias: 'widget.trolleToolbar',
    items: [
        {
            text: 'Project',
            menu: {
                items: [
                    {
                        text: 'New Project',
                        iconCls: 'add'
                    },
                    {
                        text: 'Edit Project',
                        iconCls: 'edit'
                    },
                    '-',
                    {
                        text: 'Close Project',
                        iconCls: 'close'
                    }
                ]
            }
        }
    ]
});