# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': """
        Aplicacio que gestiona un hospital""",

    'description': """
        Gestio d'un hospital
    """,

    'author': "Odoo Team 4",
    'website': "https://odoocdn.com/openerp_website/static/src/img/assets/png/odoo_logo.png?a=b",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'ERPSYSTEM',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/vistaprincipal.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    
    'installable' : True,
    'application' : True,
    'auto_install': False,
}