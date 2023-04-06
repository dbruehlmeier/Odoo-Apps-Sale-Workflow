{
    "name": "Sale Order Project Key",
    "summary": """
        Link name and analytic account with the assigned project.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Sales",
    "version": "15.0.1.5.0",
    "license": "AGPL-3",
    "depends": ["sale_timesheet", "project_key_link_type"],
    "data": ["views/sale_order.xml", "views/project_project.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
