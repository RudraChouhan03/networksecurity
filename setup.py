'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines() # Read lines from the file
            for line in lines: # Process each line
                requirement=line.strip()   
                if requirement and requirement!= '-e .': # ignore empty lines and -e .
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Krish Naik",
    author_email="krishnaik06@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)