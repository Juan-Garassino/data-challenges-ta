## Objective

Create your first CI pipeline

## Observe your first CI pipeline

Normally here you should just sit and observe.

1. Go to the GitHub Page of the repository you created in the last exercices
2. Click on `Actions` which is the GitHub name for CI-CD `actions`
3. click on your latest commit, you should see that GitHub executed your CI pipeline for you

💡 How on earth did it happen ?
 👉 `packgenlite` created for you a file under `.github/workflows/pythonpackage.yml` at the root of your package.

```yaml
name: Python package

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.6, 3.7]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v1
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Install package and test
      run: |
        make install test clean
```

With this yaml file (see yaml as a config file just like a json file in python):
 👉 every time you push a modification to master, the CI pipeline above will execute the following steps
- Get a docker image with ubuntu installed
- Install python 3
- Upgrade pip and install requirements
- Run `make install test clean`, meaning:
  => install the package
  => run the tests
- Stops if any of preceding steps failed

**NB: Here we setup the CI part of the CI/CD lifecycle of a software, we can easily imagine that once GitHub passed all the tests, you want to deploy your code somewhere, that you will see in next exercice**
