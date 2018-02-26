from odoo import models, fields

class artistas(models.Model):
    _name = 'artistas.artistas'
    nombre = fields.Char('Nombre Artista', required=True)
    genero = fields.Char('Genero Principal', required=True)
    edad = fields.Integer('Edad', required=True)