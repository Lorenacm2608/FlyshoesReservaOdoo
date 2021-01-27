# Hecho por Nadir

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

class Producto(models.Model):
    _name = 'flyshoesreserva.producto'
    
    modelo = fields.Char(String="Producto")
    descripcion = fields.Text()
    tipo = fields.Selection(selection=[
                            ('ropa', 'ROPA'),
                            ('zapatillas', 'ZAPATILLAS')
                            ])
    precio = fields.Float(required=True)
    imagen = fields.Binary(String="Imagen del producto")
    stock = fields.Integer(String="Cantidad en el almacen")
    talla = fields.Selection(selection=[
                             ('talla36', '36'),
                             ('talla37', '37'),
                             ('talla38', '38'),
                             ('talla39', '39'),
                             ('talla40', '40'),
                             ('talla41', '41'),
                             ('talla42', '42'),
                             ('talla43', '43'),
                             ('talla44', '44'),
                             ('talla45', '45'),
                             ('talla46', '46'),
                             ('xs', 'XS'),
                             ('s', 'S'),
                             ('m', 'M'),
                             ('l', 'L'),
                             ('xl', 'XL')
                             ])
    #relacion de producto->reserva                         
    reservas = fields.One2many('flyshoesreserva.reserva', 'producto', string="Reservas", required=True)
  
    #relacion de producto->proveedor
    proveedor = fields.Many2one('flyshoesreserva.proveedor', String="Proveedor", required=True)
    
    # Control del campo modelo (Producto)
    @api.constrains('modelo')
    def _verify_size_modelo(self):        
        if len(self.modelo) < 1:
            raise ValidationError("Campo modelo muy corto")
        
    # Control del campo descripcion (Producto)
    @api.constrains('descripcion')
    def _verify_size_descripcion(self):        
        if len(self.descripcion) < 1:
            raise ValidationError("Campo descripcion muy corto")
    
    # Control del precio del producto
    @api.onchange('precio')
    def _verify_valid_precio(self):
        if self.precio <= 0:
            self.precio = 1
            return {'warning': {'title': "precio 'precio' error",
                'message': "El precio que desea introducir es incorrecta",
                },
            }
        elif self.precio >= 99999:
            self.precio = 1
            return{'warning':{'title':"precio 'precio' error.",
                'message':"No puedes poner un precio tan elevado",
                },
        }
    
    # Control del stock del producto
    @api.onchange('stock')
    def _verify_valid_stock(self):
        if self.stock <= 0:
            self.stock = 1
            return {'warning': {'title': "stock 'stock' error",
                'message': "Tiene que haber al menos 1 producto",
                },
            }
        elif self.stock >= 99999:
            self.stock = 1
            return{'warning':{'title':"stock 'stock' error.",
                'message':"No puede haber tanta cantidad de un mismo producto",
                },
        }
    
    
    # Verifica la talla dependiendo el tipo del producto(Producto)
    @api.constrains('talla')
    def _tipo_producto(self): 
        if self.tipo == "ROPA" or self.tipo=="ropa":
            if self.talla == "36" or self.talla == "talla36" or self.talla == "37" or self.talla == "talla37" or self.talla == "38" or self.talla == "talla38" or self.talla == "39" or self.talla == "talla39" or self.talla == "40" or self.talla == "talla40" or self.talla == "41" or self.talla == "talla41" or self.talla == "42" or self.talla == "talla42" or self.talla == "43" or self.talla == "talla44" or self.talla == "45" or self.talla == "talla45" or self.talla == "46" or self.talla == "talla46":
                raise ValidationError("INCORRECTO, introduzca bien los datos")
        else :
            if self.talla == "XS" or self.talla=="xs" or self.talla == "S" or self.talla=="s" or self.talla == "M" or self.talla=="m" or self.talla == "l" or self.talla=="l" or self.talla == "XL" or self.talla=="xl":
                raise ValidationError("INCORRECTO, introduzca bien los datos")
    