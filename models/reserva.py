# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


from odoo import fields
from odoo import models

class Reserva(models.Model):
    _name = 'flyshoesreserva.reserva'
    name = fields.Char(string="Reserva")
    descripcion = fields.Text(required=True)
    cantidad = fields.Integer(required=True, string="Cantidad del producto")
    #fecha de entrega
    date_entrega = fields.Date(required=True, string="Fecha de entrega")
    estado_reserva = fields.Selection(selection=[('cancelada', 'CANCELADA'),
                                      ('confirmada', 'CONFIRMADA'),
                                      ('finalizada', 'FINALIZADA')],
                                      string="Estado de la reserva",
                                      help="Por favor seleciona el estado de la reserva.",
                                      default='confirmada')
                                      
    #relacion reserva->usuario(cliente)
    cliente = fields.Many2one('res.users',
                              ondelete='cascade', string="Cliente", required=True)
    #relacion reserva->producto
    producto = fields.Many2one('flyshoesreserva.producto',
                               ondelete='cascade', string="Producto", required=True)
    

    