from odoo import api, fields, models


class VisaProcess(models.Model):
    _name = "x_visa_process"
    _description = "Visa Process"
    _order = "id desc"

    x_id_number = fields.Char(string="ID Number")
    x_application_typed_date = fields.Date(string="Application Typed Date")
    x_candidate_name = fields.Char(string="Candidate Name", required=True)
    x_passport_number = fields.Char(string="Passport Number", required=True)
    x_nationality = fields.Char(string="Nationality")
    x_responsible_pro = fields.Char(string="Responsible PRO")

    x_stage = fields.Selection(
        [
            ("01_mohre_offer", "01 MOHRE Offer Letter"),
            ("02_dic_insurance", "02 DIC Insurance"),
            ("03_work_permit", "03 Work Permit"),
            ("04_entry_visa", "04 Entry Visa"),
            ("05_medical", "05 Medical"),
            ("06_tawjeeh_class", "06 Tawjeeh Class"),
            ("07_tawjeeh_submission", "07 Tawjeeh Submission"),
            ("08_eid_typing", "08 Emirates ID Typing"),
            ("09_biometric", "09 Biometric"),
            ("10_visa_stamping", "10 Visa Stamping"),
            ("11_completed", "11 Completed"),
        ],
        string="Current Stage",
        default="01_mohre_offer",
        required=True,
    )

    x_expiry_date = fields.Date(string="Expiry Date")
    x_days_remaining = fields.Integer(
        string="Days Remaining",
        compute="_compute_days_remaining",
        store=True,
        readonly=True,
    )

    @api.depends("x_expiry_date")
    def _compute_days_remaining(self):
        today = fields.Date.today()
        for record in self:
            if record.x_expiry_date:
                record.x_days_remaining = (record.x_expiry_date - today).days
            else:
                record.x_days_remaining = 0

    def action_recompute_days_remaining(self):
        records = self.search([])
        for record in records:
            record._compute_days_remaining()
        return True
