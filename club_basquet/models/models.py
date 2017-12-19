# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class club_basquet(models.Model):
#     _name = 'club_basquet.club_basquet'
#     name = fields.Char(string="Nom", required=True)
#     description = fields.Text()

class club_basquet_equip(models.Model):
    _name = "club_basquet.equip"
    nom = fields.Char(string="Nom", required=True)
    color = fields.Char(string="Color")
    patrocinador = fields.Char(string="Patrocinador")

class club_basquet_entrenador(models.Model):
    _name = "club_basquet.entrenador"
    nom = fields.Char(string="Nom")
    dni = fields.Char(string="DNI", required=True, size=9)

class club_basquet_jugador(models.Model):
    _name = "club_basquet.jugador"
    nom = fields.Char(string="Nom")
    dni = fields.Char(string="DNI", required=True, size=9)

class club_basquet_caricatura(models.Model):
    _name = "club_basquet.caricatura"
    descripcio = fields.Text(string="Descripció")

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
