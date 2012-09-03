Ext.define('Trolle.controller.User', {
    extend: 'Ext.app.Controller',

    stores: ['Users'],

    refs: [{
        ref: 'usersList'
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
        // var sourcesStore = this.getUsersStore();
        // sourcesStore.load({
        //     callback: this.onUsersLoad,
        //     scope: this
        // });
    },

    onUsersLoad: function() {
    }
});







