## responsible for creating ML project as a package and can even deploy in pypi
## it will go and check folders with __init__.py and takes that source as a package and build it
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function returns the list of requirements
    '''
    requiremnets = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requiremnets = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requiremnets:
            print("saw -e .")
            requiremnets.remove(HYPEN_E_DOT)

    return requiremnets


setup(
name='mlproject',
version='0.0.1',
author='atest',
author_email='test@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
