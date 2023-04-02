from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements = [ req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
setup(
    name='RegressorProject',
    version='0.0.1',
    author='Shubh',
    author_emails = 'shubhamnv2@gmail.com',
    install_requires =get_requirements('requirements.txt'),
    packages=find_packages(),

)