### setup.py file
from setuptools import setup

with open("requirements.txt", "r") as fh:
    requirements = fh.readlines()
    setup(
        name='eggs',
        author='PieroProietti',
        description='Port di eggs in python',
        version='0.0.1',
        packages={'penguins-eggs2'},
        install_requires=[req for req in requirements if req[:2] != "# "],
        include_package_data=True,
        entry_points={
            'console_scripts': [
                'eggs = eggs.docopt:main'
            ]
        }
    )
