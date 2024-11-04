{
    'name': 'Whatsapp API Handler',
    'author': 'Muhammad Ahmad',
    'license': 'LGPL-3',
    'version': '16.0.1.0',
    'depends': ['mail', 'web'],
    'data': [
        'security/ir.model.access.csv',

        'wizard/base_url_editor.xml',
        'wizard/templates_editor.xml',
        'wizard/login_menu.xml',
        'wizard/sync_editor.xml',

        'views/connections.xml',
        'views/menu.xml'
    ],
    'assets': {
        'web.assets_backend': ['gts_whatsapp/static/src/scss/style.scss']
    },
    'installable': True,
}