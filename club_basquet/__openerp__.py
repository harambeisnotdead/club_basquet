# -*- coding: utf-8 -*-
{
    'name': "club_basquet",

    'summary': """
        Modulo para la gestion de un club de basquet
    """,

    'description': """
        Modulo para odoo9 orientado a la gestion de un club de basquet con varios
        equipos, jugadores, entrenadores, etc.
    """,

    'author': "Saúl, Cristian i Sergi",
    'website': "http://www.exemple.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
