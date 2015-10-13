from openerp import models, fields, api, exceptions, _


class Product(models.Model):
    _inherit = "product.template"

    @api.one
    @api.constrains('name')
    def _check_name(self):
        count = self.search_count([("name", "=", self.name)])
        if count > 1:
            raise exceptions.ValidationError(_("Product %s already exist!" % self.name))
