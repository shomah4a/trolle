Ext.define('Trolle.controller.Document', {
    extend: 'Ext.app.Controller',

    views: [
        'DocumentPanel',
        'SourceTree'
    ],

    requires: [
        'Ext.Array'
    ],

    refs: [
        {
            ref: 'sourceTree',
            selector: 'sourcetree'
        },
        {
            ref: 'tabPanel',
            selector: '#document-tab-panel'
        },
        // {
        //     ref: 'panels',
        //     selector: '#document-tab-panel documentpanel'
        // }

    ],

    stores: ['Document'],

    init: function() {
        this.control({
            'sourcetree': {
                itemclick: this.doSelect
            }
        });
    },

    ////////////////////////////////////////////////////////////////
    // event handlers
    doSelect: function(me, record, elem, index, event, opts) {
        var name = record.get('name'),
            path = record.get('path');

        this.openPanel(name, path, 1);

    },

    ////////////////////////////////////////////////////////////////
    // business logics
    openPanel: function(name, path, lineNo) {
        var tabPanel = this.getTabPanel(),
            panel = this.getPanel(path);
        if (Ext.isEmpty(panel)) {
            panel = this.loadPanel(name, path);
            tabPanel.add(panel);
        };

        tabPanel.setActiveTab(panel);
    },

    getPanel: function(path) {
        return this.getTabPanel().getComponent(path);
    },

    loadPanel: function(name, path) {
        var store = Ext.create('Trolle.store.Document', {});

        var panel = Ext.create('Trolle.view.DocumentPanel', {
            title: name,
            store: store,
            itemId: path
        });

        return panel;

        // store.load({
        //     callback: function(Document) {
        //     },
        //     scope: this
        // });
    },


    // loadPanel: function(path,

    // createPanel: function(path, callback) {
    //     var store = this.getDocumentsStore();
    //     store.load({
    //         callback: callback,
    //         scope: this
    //     });
    //     // var Document = Ext.ModelMgr.getModel('Trolle.model.Document');
    //     // var doc = null;
    //     // Document.load("fork.c", {
    //     //     success: function(document) {
    //     //         doc = document;
    //     //     }
    //     // });

    //     // var panel = Ext.create('Trolle.view.DocumentPanel', {
    //     //     data: doc,
    //     //     itemId: path
    //     // });

    //     // return panel;

    //     var store = Ext.create('Trolle.store.Document', {
    //     });

    //     var panel = Ext.create('Trolle.view.DocumentPanel', {
    //         store: store,
    //         itemId: path
    //     });

    //     // return panel;
    // },



    // getPanels: function() {
    //     return this.getTabPanel();
    // }

    // init: function() {
    //     // this.control({
    //     //     'roles': {
    //     //         itemcontextmenu: this.onItemContextMenuClick,
    //     //         itemclick: this.onItemClick
    //     //     }
    //     // });
    // },

    // onLaunch: function() {
    //     // var documentsStore = this.getDocumentsStore();
    //     // documentsStore.load({
    //     //     callback: this.onDocumentsLoad,
    //     //     scope: this
    //     // });
    // },

    // onDocumentsLoad: function() {
    // }
});