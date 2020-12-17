# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import fields
from odoo import models


class Usuario(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'
    
    tipo_usuario = fields.Selection(selection=[('cliente', 'CLIENTE'),
                                    ('vendedor', 'VENDEDOR'),
                                    ('administrador', 'ADMINISTRADOR')],
                                    string="Tipo de usuario",
                                    help="Por favor seleciona el tipo de usuario.",
                                    default='cliente')
    estado_usuario = fields.Selection(selection=[('enabled', 'ENABLED'),
                                      ('disabled', 'DISABLED')],
                                      string="Tipo de usuario",
                                      help="Por favor seleciona ENABLED/DISABLED.",
                                      default='enabled')
    #relacion de cliente->reserva
    reservas_cliente = fields.One2many('flyshoesreserva.reserva', 'cliente', string="Reservas")
    
    #relacion de administrador->vendedor
    vendedores_administrador = fields.One2many('res.users', 'administrador', string="Vendedores")
    administrador = fields.Many2one('res.users',
                                    ondelete='cascade', string="Vendedor", required=True)
    
    #relacion de vendedor->cliente
    clientes_vendedor = fields.One2many('res.users', 'vendedor', string="Clientes")
    vendedor = fields.Many2one('res.users',
                               ondelete='cascade', string="Cliente", required=True)
    
    #relacion de administrador->proveedor
    proveedores_administrador = fields.One2many('flyshoesreserva.proveedor', 'p_administrador', string="Proveedores")
    
    #relacion de vendedor->producto
    productos_vendedor = fields.Many2many('flyshoesreserva.producto', String="Productos")
    
    