#!/usr/bin/env python
# -*- coding: utf-8 -*-

from odoo import models, fields

class musica(models.Model):
    _name = 'musica.musica'
    cancion = fields.Char('Cancion', required=True)
    genero = fields.Char('Genero', required=True)
    anniosalida = fields.Integer('Año Salida', required=True)