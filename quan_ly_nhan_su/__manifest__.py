{
    'name': 'Quản lý nhân sự',
    'version': '1.0',
    'summary': 'Module quản lý nhân sự cho công ty',
    'description': 'Module quản lý thông tin nhân viên, phòng ban, hợp đồng, chấm công, lương thưởng, và các thông tin liên quan.',
    'author': 'Tên của bạn',
    'website': 'https://www.côngty.com',
    'category': 'Human Resources',
    'depends': ['base', 'mail'],  # Phụ thuộc vào module base và mail
    'data': [
        'security/security.xml',  # Load trước
        'security/ir.model.access.csv',  # Load sau
        'data/department_data.xml',
        'data/employee_data.xml',
        'views/employee_views.xml',
        'views/department_views.xml',
        'views/contract_views.xml',
        'views/attendance_views.xml',
        'views/payroll_views.xml',
        'views/menus.xml',
        'reports/employee_report.xml',
        'reports/payroll_report.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'hr_management/static/src/css/styles.css',
            'hr_management/static/src/js/scripts.js',
        ],
    },
}