"""Setup script.

Run "python3 setup --help-commands" to list all available commands and their
descriptions.
"""
import os
from subprocess import call
from setuptools import Command, find_packages, setup


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""

    user_options = []

    def initialize_options(self):
        """No initializa options."""
        pass

    def finalize_options(self):
        """No finalize options."""
        pass

    def run(self):
        """Clean build, dist, pyc and egg from package and docs."""
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.egg-info')
        os.system('cd docs; make clean')


class Linter(Command):
    """Run several code linters."""

    description = 'Run many code linters. It may take a while'
    user_options = []

    def __init__(self, *args, **kwargs):
        """Define linters and a message about them."""
        super().__init__(*args, **kwargs)
        self.linters = ['pep257', 'pyflakes', 'mccabe', 'isort', 'pep8',
                        'pylint']
        self.extra_msg = 'It may take a while. For a faster version (and ' \
                         'less checks), run "quick_lint".'

    def initialize_options(self):
        """For now, options are ignored."""
        pass

    def finalize_options(self):
        """For now, options are ignored."""
        pass

    def run(self):
        """Run pylama and radon."""
        files = 'tests setup.py pyof'
        print('running pylama with {}. {}'.format(', '.join(self.linters),
                                                  self.extra_msg))
        cmd = 'pylama -l {} {}'.format(','.join(self.linters), files)
        call(cmd, shell=True)
        print('Low grades (<= C) for Cyclomatic Complexity:')
        call('radon cc --min=C ' + files, shell=True)
        print('Low grades (<= C) for Maintainability Index:')
        call('radon mi --min=C ' + files, shell=True)


setup(name='pycccl',
      version="0.1.1",
      description='Python (C)rypto (C)urrency (C)ommon (L)ibrary.',
      url='http://github.com/beraldoleal/pycccl',
      author='Beraldo Leal',
      author_email='beraldo@gmail.com',
      license='MIT',
      packages=find_packages(exclude=[]),
      cmdclass={
          'lint': Linter,
          'clean': CleanCommand,
      },
      zip_safe=False)
