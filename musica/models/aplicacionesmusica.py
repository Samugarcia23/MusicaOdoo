#!/usr/bin/env python
# -*- coding: utf-8 -*-

from odoo import models, fields

class aplicacionesmusica(models.Model):
    _name = 'aplicacionesmusica.aplicacionesmusica'
    nombre = fields.Char('Nombre App', required=True)
    plataforma = fields.Char('Plataforma', required=True)
    annioSalida = fields.Integer('Año Salida', required=True)