# Copyright 2018 FOREST AND BIOMASS ROMANIA SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class Project(models.Model):
    _inherit = "project.project"

    event_ids = fields.One2many('event.event', 'x_studio_many2one_field_oQRjs', string="Évènements")
    count_event = fields.Integer(string="Évènements", compute='count_events', store=True)

    @api.depends('event_ids')
    def count_events(self):
        for rec in self:
            if rec.event_ids:
                rec.count_event = len(rec.event_ids)
