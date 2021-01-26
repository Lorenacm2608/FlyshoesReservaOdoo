# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# Fredy Vargas Flores

from datetime import datetime
from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError



class Reserva(models.Model):
    _name = 'flyshoesreserva.reserva'
    name = fields.Char(required=True, string="Reserva")
    descripcion = fields.Text(required=True)
    cantidad = fields.Integer(required=True, default=1, string="Cantidad del producto")
    
    date_entrega = fields.Date(required=True, string="Fecha de entrega")
    estado_reserva = fields.Selection(selection=[('cancelada', 'CANCELADA'),
                                      ('confirmada', 'CONFIRMADA'),
                                      ('realizada', 'REALIZADA'),
                                      ('expirada', 'EXPIRADA')],
                                      string="Estado de la reserva",
                                      help="Por favor seleciona el estado de la reserva.",
                                      default='confirmada')

    # relacion reserva->usuario(cliente)
    cliente = fields.Many2one('res.users',
                              ondelete='cascade', string="Cliente", required=True)
    # relacion reserva->producto
    producto = fields.Many2one('flyshoesreserva.producto',
                               ondelete='cascade', string="Producto", required=True)
                               
    
    
    # Control de la cantidad del producto
    @api.onchange('cantidad')
    def _verify_valid_cantidad(self):
        if self.cantidad < 1:
            self.cantidad = 1
            return {'warning': {'title': "Cantidad 'cantidad' error",
                'message': "La cantidad que desea reservar es incorrecta",
                },
            }
        elif self.cantidad > 10:
            self.cantidad = 10
            return{'warning':{'title':"Cantidad 'cantidad' error.",
                'message':"No puedes reservar mas de 10 unidades",
                },
        }
            
    # Validacion de la fecha de entrega        
    @api.constrains('date_entrega')
    def _verify_date_entrega(self):
        hoy = datetime.now().date()
        parametro = self.date_entrega
        entrega = datetime.strptime(str(parametro), '%Y-%m-%d')
        if str(entrega) < str(hoy):
            raise ValidationError("Fecha de entrega introducida es incorrecta")
        
    # Control de la longitud del campo descripcion   
    @api.constrains('descripcion')
    def _verify_size_descripcion(self):        
        if len(self.descripcion) < 10:
            raise ValidationError("Campo descripcion muy corta")
    
    # Control del campo name (Reserva)
    @api.constrains('name')
    def _verify_size_name(self):        
        if len(self.name) < 5:
            raise ValidationError("Campo reserva muy corta")
        
    # Actualizar producto stock (Producto)
    @api.constrains('estado_reserva')
    def _update_stock_producto(self):
        if self.estado_reserva == "CONFIRMADA":
            producto_stock = self.producto.stock
            if self.cantidad < producto_stock:
                self.producto.stock = producto_stock - self.cantidad
            else:
                return{'warning':{'title':"Cantidad 'cantidad' error.",
                    'message':"No hay stock del producto seleccionado",
                    },
            }
        elif self.estado_reserva == "CANCELADA":
            self.producto.stock = producto_stock + self.cantidad
                
            
                
            
