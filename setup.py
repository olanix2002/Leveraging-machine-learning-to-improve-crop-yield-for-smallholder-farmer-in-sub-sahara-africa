from setuptools import setup, find_packages,setup 
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    This function reads the requirements.txt file and returns a list of requirements
    '''
    requirements = []
    with open(file_path,'r') as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements         


setup(name='crop_yield_ml',
      version='0.0.1',
      description='ML in production',
      author='Abdulwajeed',
      author_email='ganiyuabdulwajeed2002@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt')
      
      
      )
