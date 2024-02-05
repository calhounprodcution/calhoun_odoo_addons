{
    'name': 'Purchase Discount',
    'version': '1.0',
    'description': 'Apply Discount In Purchase Order Same As Sale Order',
    'summary': 'Apply Discount In Purchase Order Same As Sale Order',
    'author': 'PT Calhoun Production',
    'website': 'https://google.com',
    'license': 'LGPL-3',
    'category': 'Inventory/Purchase',
    'depends': [
        'purchase'
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/purchase_order_discount_views.xml',
        'views/purchase_views.xml',
    ],
    'demo': [],
    'auto_install': False,
    'application': False,
    'assets': {}
}