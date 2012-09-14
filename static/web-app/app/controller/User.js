Ext.define('Trolle.controller.User', {
    extend: 'Ext.app.Controller',

    stores: ['Users'],

    refs: [{
        ref: 'usersList',
        selector: 'userlist'
    }],

    ////////////////////////////////////////////////////////////////
    // event handlers

    ////////////////////////////////////////////////////////////////
    // business logics
    joinUser: function(user) {
        var userList = this.getUserList();
    },

    leftUser: function(user) {

    },

});