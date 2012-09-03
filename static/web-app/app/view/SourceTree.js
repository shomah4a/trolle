Ext.define('Trolle.view.SourceTree', {
    extend: 'Ext.tree.Panel',

    alias: 'widget.sourcetree',

    store: 'SourceInfos',

    rootVisible: false,

    lines: true,

    useArrows: true
    // collapsible: true,
});