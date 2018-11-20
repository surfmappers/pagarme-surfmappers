from distutils.core import setup

requires = [i.strip() for i in open("requirements.txt").readlines()]

setup(name='pagarme-surfmappers',
      version='1.0',
      description='Simple Pagar.me module made by Surfmappers.com',
      author='Yuri Alessandro Martins',
      author_email='yuri@surfmappers.com',
      url='',
      install_requires=requires,)
