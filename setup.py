from setuptools import setup, find_packages

def get_requirements(file):
    requirements=[]
    with open(file) as f:
        requirements=f.read().splitlines()

setup(name='Ml_project',version='0.0.1',author='Hicham',author_email="hichamalaoui975@gmail.com",packages=find_packages(),install_requires=get_requirements('requirements.txt'),zip_safe=False)