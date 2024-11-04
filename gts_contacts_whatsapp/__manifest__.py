{
    'name': 'Import Whatsapp Contacts in Odoo',
    'description': 'static/description/index.html',
    'author': 'WLink',
    'license': 'LGPL-3',
    'version': '18.0.1.0',
    'depends': ['gts_whatsapp', 'contacts', 'sale'],
    'images': ['static/description/banner.png'],
    'data': [
        'security/ir.model.access.csv',

        'wizard/message_menu.xml',

        'views/menu.xml'
    ],
    'installable': True,
    'application': False
}
