from setuptools import setup

setup(name='notes-py',
      version='0.0.1',
      packages=['notes'],
      entry_points={
          'gui_scripts': [
              'notes = notes.__main__:main'
          ]
      })
