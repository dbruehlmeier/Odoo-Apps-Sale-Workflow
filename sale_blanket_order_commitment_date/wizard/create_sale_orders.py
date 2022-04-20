from odoo import _, api, fields, models
import logging
_logger = logging.getLogger(__name__)


class BlanketOrderWizard(models.TransientModel):
    _inherit= "sale.blanket.order.wizard"

    def _prepare_so_line_vals(self, line):
        res = super(BlanketOrderWizard, self)._prepare_so_line_vals(line)
        res.update(
            {
                "commitment_date": line.date_schedule
            }
        )
        return res