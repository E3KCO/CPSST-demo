# Copyright 2018 FOREST AND BIOMASS ROMANIA SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class Event(models.Model):
    _inherit = "event.event"

    x_studio_many2one_field_oQRjs = fields.Many2one('project.project', string="Projet")

    def name_get(self):
        """ Custom name_get implementation to better differentiate dates

          * name, date is not set -> take name
          * both have name: name + date
        """
        ret_list = []
        for event in self:
            if event.date_begin:

                name = '%s - %s' % (event.name, event.date_begin.date())
            else:
                name = event.name
            ret_list.append((event.id, name))
        return ret_list
