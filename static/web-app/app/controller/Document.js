Ext.define('Trolle.controller.Document', {
    extend: 'Ext.app.Controller',

    requires: [
        'Trolle.ux.Router'
    ],

    stores: ['Document'],

    views: [
        'DocumentPanel',
        'Outline',
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
        {
            ref: 'outline',
            selector: 'outline'
        },

        // {
        //     ref: 'panels',
        //     selector: '#document-tab-panel documentpanel'
        // }

    ],

    init: function() {
        this.control({
            'sourcetree': {
                itemclick: this.doSelectDocument
            },
            'outline': {
                itemclick: this.doSelectOutline
            }
        });
    },

    ////////////////////////////////////////////////////////////////
    // event handlers
    doSelectDocument: function(me, record, elem, index, event, opts) {
        if (record.get('leaf')) {
            var path = record.get('path');

            this.openPanel(path);
        }
    },

    doSelectOutline: function(me, record, elem, index, event, opts) {
        this.gotoLine(record.get('lineNo'));
    },

    doIndex: function() {
    },

    doViewDocument: function(path) {
        this.openPanel(path);
    },

    // doChangeURI: function(token) {
    //     this.openPanel(token);
    // },

    // doChangeHash: function(hash) {
    //     this.gotoLine(hash);
    // },

    ////////////////////////////////////////////////////////////////
    // business logics
    openPanel: function(path) {
        var name = this.getFileName(path),
            tabPanel = this.getTabPanel(),
            outline = this.getOutline(),
            panel = this.getPanel(path);

        if (Ext.isEmpty(panel)) {
            panel = this.loadPanel(name, path);
            tabPanel.add(panel);
        };

        tabPanel.setActiveTab(panel);
    },

    addHistory: function(path) {
        Trolle.ux.Router.pushState(null, path, path);
    },

    getFileName: function(path) {
        return String(path).substring(path.lastIndexOf("/") + 1);
    },

    gotoLine: function(lineNo) {
        lineNo = parseInt(lineNo);
        if (!isNaN(lineNo)) {
            return;
        }

    },

    getCurrentPanel: function() {
        return this.getTabPanel().getActiveTab();
    },

    getPanel: function(path) {
        return this.getTabPanel().getComponent(path);
    },

    loadPanel: function(name, path) {
        var me = this,
            outline = this.getOutline(),
            outlineData;

        var documentStore = Ext.create('Trolle.store.Document', {
                listeners: {
                    load: function() {
                        outlineData = documentStore.getProxy().reader.jsonData['outline'];
                        outline.setRootNode(outlineData);
                    }
                }
            });

        var documentPanel = Ext.create('Trolle.view.DocumentPanel', {
                title: name,
                toolTip: path,
                store: documentStore,
                itemId: path,
                listeners: {
                    added: function() {
                        me.addHistory(path);
                    },
                    activate: function(it, opts) {
                        outline.setRootNode(outlineData);
                        me.addHistory(path);
                    }
                }
            });

        return documentPanel;
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