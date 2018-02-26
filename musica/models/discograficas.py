from odoo import models, fields

class discograficas(models.Model):
    _name = 'discograficas.discograficas'
    nombre = fields.Char('Nombre Discografica', required=True)
    genero = fields.Char('Genero Principal', required=True)
    numartistas = fields.Integer('Numero de Artistas', required=True)