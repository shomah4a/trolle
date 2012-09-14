Ext.define('Trolle.view.Outline', {
    extend: 'Ext.tree.Panel',

    alias: 'widget.outline',

    store: 'Outlines',

    rootVisible: false,

    lines: false,

    setRootNode: function(node) {
        this.getStore().setRootNode(Ext.clone(node));
    }
});