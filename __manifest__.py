# -*- coding: utf-8 -*-
{
    'name': "tdsiIUT",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "teamDSI",
    'website': "http://www.team-dsi.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/helico/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/tdsimodel_security.xml',
        'datas/datas.xml',
        'views/views.xml',
        'views/iut_it_brand_views.xml',
        'views/iut_it_device_views.xml',
        'views/iut_it_model_type.xml',
        'views/iut_it_model_views.xml',
        'views/iut_it_office_views.xml',
        'views/iut_room.xml',
        'views/iut_res_partner.xml',
        'tdsimodel_menu.xml',
        'iut_brand_menu.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
