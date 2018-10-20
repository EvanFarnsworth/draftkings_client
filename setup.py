
from setuptools import setup, find_packages
setup(
  name='draft_kings',
  packages=find_packages(exclude=['tests*']),
  install_requires=['requests', 'enum34'],
  version='1.0',
  description='A DraftKings client',
  author='Jae Bradley',
  author_email='jae.b.bradley@gmail.com',
  keywords=['sports', 'dfs', 'draftkings', 'draft kings'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 3.6',
  ],
)