from odoo import models, api


class QuickRecordSearch(models.AbstractModel):
    _name = "quick.record.search"
    _description = "Quick Record Search"

    @api.model
    def record_search(self, model, term, limit=10):
        try:
            Model = self.env[model]
        except Exception:
            return []
        try:
            Model.check_access_rights("read")
        except Exception:
            return []
        records = Model.sudo().search([("display_name", "ilike", term)], limit=limit)
        results = []
        for rec in records:
            results.append(
                {
                    "id": rec.id,
                    "name": rec.display_name,
                    "url": f"/web#id={rec.id}&model={model}&view_type=form",
                }
            )
        return results
