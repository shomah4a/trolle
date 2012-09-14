Ext.application({
    name: 'Trolle',

    autoCreateViewport: true,

    paths: {
        'Ext.ux': 'app/ux'
    },

    requires: [
        'Trolle.ux.Router',
        'Ext.util.History',
        'Ext.EventManager'
    ],

    mixins: {
        observable: 'Ext.util.Observable'
        // router: 'Trolle.ux.Router'
    },

    models: [
        'Document',
        'SourceInfo',
        'Outline',
        'User',
        'Log'
    ],

    stores: [
        'Document',
        'SourceInfos',
        'Outlines',
        'Users',
        'Logs'
    ],

    controllers: [
        'Document',
        'SourceInfo',
        'Outline',
        'User',
        'Log'
    ],

    views: [],

    init: function(config) {
        Trolle.ux.Router.init(this);
        this.listenEvents();
    },

    listenEvents: function() {
        window.onbeforeunload = function(e) {
            return '';
        };
    },

    // routeing
    routes: {
        '/': 'Document.doIndex',
        '$path': 'Document.doViewDocument'
    }
});