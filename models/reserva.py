# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# Fredy

from datetime import datetime
from datetime import timedelta
from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError



class Reserva(models.Model):
    _name = 'flyshoesreserva.reserva'
    name = fields.Char(required=True, string="Reserva")
    descripcion = fields.Text(required=True)
    cantidad = fields.Integer(required=True, default=1, string="Cantidad del producto")
    # nombre_producto = fields.Text(related='producto.modelo')
    # fecha de entrega
    date_entrega = fields.Date(required=True, string="Fecha de entrega")
    estado_reserva = fields.Selection(selection=[('cancelada', 'CANCELADA'),
                                      ('confirmada', 'CONFIRMADA'),
                                      ('finalizada', 'FINALIZADA')],
                                      string="Estado de la reserva",
                                      help="Por favor seleciona el estado de la reserva.",
                                      default='confirmada')

    # relacion reserva->usuario(cliente)
    cliente = fields.Many2one('res.users',
                              ondelete='cascade', string="Cliente", required=True)
    # relacion reserva->producto
    producto = fields.Many2one('flyshoesreserva.producto',
                               ondelete='cascade', string="Producto", required=True)
                               
    #https://github.com/Odoo-10-test/trucos_odoo/blob/master/modelos.md    
    #https://www.flashodoo.com/blog/flashodoo-1/post/trucos-de-odoo-78
    
    @api.onchange('cantidad')
    def _verify_valid_cantidad(self):
        if self.cantidad < 1:
            self.cantidad = 1
            return {'warning': {'title': "Cantidad 'cantidad' error",
                'message': "La cantidad que desea reservar es incorrecta",
                },
            }
        else:
            if self.cantidad > 10:
                self.cantidad = 10
                return{'warning':{'title':"Cantidad 'cantidad' error.",
                    'message':"No puedes reservar mas de 10 unidades",
                    },
            }
            
            
    @api.constrains('date_entrega')
    def _verify_date_entrega(self):
        hoy = datetime.now().date()
        entrega = datetime.strptime(str(self.date_entrega), '%Y-%m-%d')
        if str(entrega) < str(hoy):
            raise ValidationError("Fecha de entrega introducida es incorrecta")
                    
    
