{
    'name': 'WLink QR Whatsapp API Base',
    'description':'static/description/index.html',
    'author': 'WLink',
    'license': 'LGPL-3',
    'version': '18.0.1.0',
    'depends': ['mail'],
    'website':'https://wlink.geektechsol.com',
    'images': ['static/description/banner_base.png'],
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
