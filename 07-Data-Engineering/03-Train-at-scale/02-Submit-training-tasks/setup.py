from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'pip>=9',
    'setuptools>=26',
    'wheel>=0.29',
    'pandas',
    'pytest',
    'coverage',
    'flake8',
    'black',
    'yapf',
    'python-gitlab',
    'twine',
    'six==1.14.0',
    'numpy==1.18.5',
    'pandas',
    'scikit-learn==0.22',
    'joblib',
    'memoized-property',
    'mlflow',
    's3fs',
    'gcsfs',
    'google-cloud-storage',
    'termcolor'
]

setup(
    name='SimpleTaxiFare',
    version='1.0',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='Taxi Fare Prediction Pipeline'
)
