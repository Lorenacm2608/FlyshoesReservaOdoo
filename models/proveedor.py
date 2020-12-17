# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#Lorena

from odoo import fields
from odoo import models
class Proveedor(models.Model):
    _name = 'flyshoesreserva.proveedor'
    
    tipo = fields.Selection(selection=[
                             ('zapatillas', 'ZAPATILLAS'),
                             ('ropa', 'ROPA')
                             ])
    empresa = fields.Char(required=True)
    email = fields.Char(required=True)
    mombre = fields.Char(required=True)
    telefono = fields.Char(required=True)
    descripcion = fields.Char()
    
    #Relacion de proveedor->usuario(Administrador)
    p_administrador = fields.Many2one('res.users', string="Administrador", required=True)
    
    #Relacion de proveedor-> producto
    producto = fields.One2many('flyshoesreserva.producto', 'proveedor', string="Productos", required=True)
