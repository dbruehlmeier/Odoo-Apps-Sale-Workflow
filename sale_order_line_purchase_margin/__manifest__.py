{
    "name": "Sale Order Line Purchase Margin",
    "summary": """
        Calculate sale line margin from linked purchase.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Sales",
    "version": "14.0.1.2.0",
    "license": "AGPL-3",
    "depends": ["sale_margin", "sale_purchase_stock"],
    "data": ["views/sale.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}