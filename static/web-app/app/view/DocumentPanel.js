Ext.define('Trolle.view.DocumentPanel', {
    extend: 'Ext.view.View',

    xtype: 'documentpanel',

    // store: 'Document',

    store: null,

    itemSelector: 'div.highlight',

    renderTo: Ext.getBody(),

    layout: {
        type: 'fix',
        align: 'stretch'
    },

    getTitle: function() {
        return this.getData().get('name');
    },

    tpl: new Ext.XTemplate(
        '<tpl for=".">',
          '<div class="highlight">',
            '<pre class="line-numbers">',
              '<tpl for="this.toLines(body)">',
                '<a href="#{parent.path}:{number}">{number}</a>',
              '</tpl>',
            '</pre>',
            '<pre class="body">',
              '<tpl for="this.toLines(body)">',
                '<p id="{parent.path}:{number}">{line}<tpl for="this.isEmpty(line)"><br/></tpl></p>',
              '</tpl>',
            '</pre>',
          '</div>',
        '</tpl>',
        {
            toLines: function(body) {
                var lines = body.split('\n');
                return Ext.Array.map(lines, function(line, index) {
                    return {
                        number: index,
                        line: Ext.htmlEncode(line)
                    };
                });
            },
            isEmpty: function(value) {
                return Ext.isEmpty(value);
            }
        }
    )
});