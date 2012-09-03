Ext.define('Trolle.controller.Outline', {
    extend: 'Ext.app.Controller',

    stores: ['Outlines'],

    refs: [{
        ref: 'outline'
    }],

    init: function() {
        // this.control({
        //     'roles': {
        //         itemcontextmenu: this.onItemContextMenuClick,
        //         itemclick: this.onItemClick
        //     }
        // });
    },

    onLaunch: function() {
        // var sourcesStore = this.getOutlinesStore();
        // sourcesStore.load({
        //     callback: this.onOutlinesLoad,
        //     scope: this
        // });
    },

    onOutlinesLoad: function() {
    }
});







