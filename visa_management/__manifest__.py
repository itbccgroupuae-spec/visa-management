{
    "name": "Visa Management",
    "version": "19.0.1.0.0",
    "category": "Human Resources",
    "summary": "Visa process tracking with Kanban, expiry days, dashboard and scheduled update",
    "author": "BCC Group International",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/visa_process_views.xml",
        "data/ir_cron.xml"
    ],
    "application": True,
    "installable": True
}
