from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
  'scikit-learn==0.20.2',
  'pandas==0.24.0',
  'google-cloud-storage',
  'gcsfs'
  ]

setup(
    name='trainer',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='My training application package.'
)