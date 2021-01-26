# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#Moroni

from odoo import fields
from odoo import models
from odoo import api
class Proveedor(models.Model):
    _name = 'flyshoesreserva.proveedor'
    
    tipo = fields.Selection(selection=[
                             ('zapatillas', 'ZAPATILLAS'),
                             ('ropa', 'ROPA')
                             ])
    empresa = fields.Char(required=True)
    email = fields.Char(required=True)
    nombre = fields.Char(required=True)
    telefono = fields.Integer(required=True, default=1, string="Telefono")
    descripcion = fields.Char()
    
    #Relacion de proveedor->usuario(Administrador)
    p_administrador = fields.Many2one('res.users', string="Administrador", required=True)
    
    #Relacion de proveedor-> producto
    producto = fields.One2many('flyshoesreserva.producto', 'proveedor', string="Productos", required=True)

# Control del telefono del proveedor
    @api.onchange('telefono')
    def _verify_valid_telefono(self):
        if (self.telefono >= 1000000000 | self.telefono <= 100000000):
            self.telefono = 1
            return {'warning': {'title': "Telefono 'telefono' error",
                'message': "El telefono introducido es incorrecto",
                },
        }