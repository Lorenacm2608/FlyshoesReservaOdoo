# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#Moroni

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

#Author: Moroni
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
    administrador = fields.Many2one('res.users', string="Administrador", required=True)
    
    #Relacion de proveedor-> producto
    producto = fields.One2many('flyshoesreserva.producto', 'proveedor', string="Productos", required=True)

# Control del campo empresa (Proveedor)
    @api.constrains('empresa')
    def _verify_size_empresa(self):        
        if len(self.empresa) < 5:
            raise ValidationError("Campo empresa muy corta")
        
        # Control del campo email (Proveedor)
    @api.constrains('email')
    def _verify_size_email(self):        
        if len(self.email) < 5:
            raise ValidationError("Campo email muy corta")
        
        
# Control del campo name (Proveedor)
    @api.constrains('nombre')
    def _verify_size_nombre(self):        
        if len(self.nombre) < 5:
            raise ValidationError("Campo proveedor muy corta")
        
# Control del telefono del proveedor
    @api.onchange('telefono')
    def _verify_valid_telefono(self):
        if (self.telefono >= 1000000000 | self.telefono <= 100000000):
            self.telefono = 1
            return {'warning': {'title': "Telefono 'telefono' error",
                'message': "El telefono introducido es incorrecto",
                },
        }
        
# Control de la longitud del campo descripcion   
    @api.constrains('descripcion')
    def _verify_size_descripcion(self):        
        if len(self.descripcion) < 10:
            raise ValidationError("Campo descripcion muy corta")