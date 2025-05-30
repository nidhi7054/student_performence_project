from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:

    '''This Function will Return a requirements '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

            return requirements

setup(
    name='my_package',
    version='0.1',
    description='A sample Python package',
    author='Nidhi',
    author_email='nrgautam7054@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)