from openerp import models, fields, api, exceptions, _


class Product(models.Model):
    _inherit = "product.template"

    @api.one
    @api.constrains('name', 'default_code')
    def _check_name(self):
        count = self.search_count([("name", "=", self.name), ("default_code", "=", self.default_code)])
        if count > 1:
            raise exceptions.ValidationError(
                _("Product %s with default_code %s already exist!") % (self.name, self.default_code))
