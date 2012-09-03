Ext.application({
    name: 'Trolle',
    autoCreateViewport: true,

    models: ['Document', 'SourceInfo', 'Outline', 'User', 'Log'],
    stores: ['Document', 'SourceInfos', 'Outlines', 'Users', 'Logs'],
    controllers: ['Document', 'SourceInfo', 'Outline', 'User', 'Log'],
    views: []
});