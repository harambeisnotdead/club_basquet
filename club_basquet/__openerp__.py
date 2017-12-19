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
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml'
    ]
}
