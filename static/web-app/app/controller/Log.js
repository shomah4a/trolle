Ext.define('Trolle.controller.Log', {
    extend: 'Ext.app.Controller',

    refs: [
        {
            ref: 'log',
            selector: 'log'
        }
    ],

    init: function() {
        // this.control({
        //     'viewpanel log': {
        //         render: this.onLogRendered
        //     }
        // });
        // this.getLog().store.load();
        // this.getLog().setValue('join guest');
    },

});
