# -*- coding: utf-8 -*-
{
    'name': "alex",

    'summary': """
        prueba alex clase 2""",

    'description': """
        como funciona
    """,

    'author': "alexanderTL",
    'website': "http://www.alex001.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'rock',
    'version': '007',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    
    # only loaded in demonstration mode
    #'demo': [
    #   'demo/demo.xml',
    #],
}
