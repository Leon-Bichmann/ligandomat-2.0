import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()


test = "test"
requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'mysql-python',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'pyramid_tm',
    'simplejson'
    ]

setup(name='HLA_Ligand_Atlas',
      version='0.1',
      description='HLA_Ligand_Atlas',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Linus Backert',
      author_email='linus.backert@uni-tuebingen.de',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='ligando',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = ligando:main
      [console_scripts]
      initialize_ligando_db = ligando.scripts.initializedb:main
      """,
      )
