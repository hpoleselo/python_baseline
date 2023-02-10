from setuptools import setup, find_packages

setup(
   name='app_name',
   version='1.0',
   description='A useful module',
   author='Henrique Poleselo',
   author_email='myemail@gmail.com',
   packages=find_packages(exclude=['test']),
   #packages=['app_utils', 'apps'],  #same as name
   install_requires=['wheel'], #external packages as dependencies
)