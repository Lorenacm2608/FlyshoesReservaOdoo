from odoo import models, fields

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
    