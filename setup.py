from setuptools import setup, find_packages

setup(
    name='custom_qty_app',
    version='0.0.1',
    description='Custom Qty modifications for Sales Order in Frappe/ERPNext',
    author='Neotec Integrated Solutions',
    author_email='noor@neotech.ai',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=('frappe',),
)
