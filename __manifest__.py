# -*- coding: utf-8 -*-
{
    'name': "flyshoesreserva",

    'summary': """
        Somos una tienda que se dedica a vender zapatillas y ropa de deporte.""",

    'description': """
        Somos una tienda que se dedica a vender zapatillas y ropa de deporte, pero como estamos en unas condiciones por la pandemia mundial, 
        hemos decidido actuar de la siguiente manera; reservar desde la aplicacion del telefono movil, ir a la tienda 
        respetando todas las medidas de seguridad y recoger la reserva hecha desde el movil.""",

    'author': "Flyshoes",
    'website': "http://www.flyshoes.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/reservas.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}