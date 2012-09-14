Ext.define('Trolle.ux.Router', (function() {

    // private members.
    var me, app_, routes_ = [];

    function processRoutes() {
        routes_ = Trolle.util.Object.map(app_.routes, function(route, value) {
            var regex = '^' + route.replace('/', '\\/').replace(/\$[a-zA-z]\w*/g, '(.+)') + '$',
                v = value.split('.'),
                controller = app_.getController(v[0]),
                action = v[1];
            if (!Ext.isEmpty(controller) && !Ext.isEmpty(action) && !Ext.isEmpty(controller[action])) {
                var handler = Ext.bind(controller[action], controller);

                return {
                    handler   : handler,
                    matcher   : new RegExp(regex)
                };
            }
        }, me);
    }

    function listenEvents() {
        window.onpopstate = function(event) {
            me.popState(window.location.pathname);
        };
    }

    function routeing(path) {
        return Trolle.util.Array.find(routes_, function(r) {
            return r.matcher.test(path);
        }, me);
    }

    return {
        singleton: true,
        requires: [
            'Ext.util.History',
            'Ext.app.Application',
            'Trolle.util.Object',
            'Trolle.util.Array'

        ],

        routes: {}, // override here.

        init: function(app) {
            me = this;
            app_ = app;
            processRoutes();
            listenEvents();
        },

        pushState: function(state, title, url) {
            if (url !== window.location.pathname) {
                if (window.history.pushState) {
                    window.history.pushState(state, title, url);
                }
            }
        },

        popState: function(path) {
            var route = routeing(path);

            if (!Ext.isEmpty(route)) {
                var args = path.match(route.matcher).slice(1);
                route.handler.apply(null, args);

            }
        }
    };
})());