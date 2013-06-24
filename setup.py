from setuptools import setup

setup(
   name='webshell',
   author = 'iBiZoNiX',
   author_email = 'iBiZoNiX@outlook.com',
   version='1.0',
   packages=['webshell'],
   package_data={
      'webshell': ['*.*','shell/*.*','webshell/*.*','shell/templates/*.*'],
   },
   description = 'Simple web shell',
   install_requires=['Django>=1.5.1'],
   zip_safe=False,
)