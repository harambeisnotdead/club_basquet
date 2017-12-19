# -*- coding: utf-8 -*-

from openerp import models, fields, api

class club_basquet_equip(models.Model):
    """
        Classe equip amb els atributs nom(Char), color(Char) i patrocinador(Char)
    """
    _name = "club_basquet.equip"
    nom = fields.Char(string="Nom", required=True)
    color = fields.Char(string="Color")
    patrocinador = fields.Char(string="Patrocinador")

class club_basquet_entrenador(models.Model):
    """
        Classe entrenador amb els atributs nom(Char) i dni(Char)
    """
    _name = "club_basquet.entrenador"
    nom = fields.Char(string="Nom")
    dni = fields.Char(string="DNI", required=True, size=9)

class club_basquet_jugador(models.Model):
    """
        Classe jugador amb els atributs nom(Char) i dni(Char)
    """
    _name = "club_basquet.jugador"
    nom = fields.Char(string="Nom")
    dni = fields.Char(string="DNI", required=True, size=9)

class club_basquet_caricatura(models.Model):
    """
        Classe caricatura amb l'atribut descripcio(Text)
    """
    _name = "club_basquet.caricatura"
    descripcio = fields.Text(string="Descripció")
