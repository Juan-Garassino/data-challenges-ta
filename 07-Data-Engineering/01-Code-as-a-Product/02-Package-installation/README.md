## Objective

Install your first package called `mlproject`

## Your first package

Now sit anywhere you want your package to live and run:
```bash
wagon-make-package mlproject
```

The ultimate goals of our `mlproject` are:
- install it as a package
- install scripts

Get inside `mlproject`  
👉 Inspect script under `scripts/mlproject-run`  
👉 Inspect code you want to package as a module under `mlproject/`  

You'll want to install these dependencies and the script.

To install your package, as seen in lecture, simply run:
```bash
pip install .
```
💡 __Here pip understands what he has to do thanks to his budy and MVP `setup.py` file__  
💡 __Thanks to his MVP, he knew he had to install dependencies from `requirements.txt`__

## Project as a package
Your mlproject is now a package, just like pandas or sklearn

Go anywhere you want and launch inside `ipython` or `python` interpreter or inside a notebook:

```python
from mlproject.lib import clean_data
```

## Project as scripts

You also have installed a script, test it:
```
mlproject-run
```

## Your first module now
Create a new python file called `mlproject/distance.py` inside which you'll add following function

```python
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r
```

To check your function works, good practice is to add `if __name__ == "__main__"` at the end of `distance.py` and compute your first distance:
```python
if __name__ == "__main__":
    # Le Wagon location
    lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    #lat2, lon2 = x, y
    distance = haversine(lon1, lat1, lon2, lat2)
    print(distance)
```
🤔Ask [Sam&Max](http://sametmax.com/pourquoi-if-__name__-__main__-en-python/) if not clear

Then run :
```bash
python -i mlproject/distance.py
```
💡 __You could also run `%run mlproject/distance.py` inside a notebook or ipython interpreter (do not forget to `import mlproject.lib`, you must be located in `mlproject/`)__

Your new tree should look like:
```bash
├── MANIFEST.in
├── Makefile
├── README.md
├── mlproject
│   ├── __init__.py
│   ├── data
│   │   └── data.csv.gz
│   ├── distance.py
│   └── lib.py
├── requirements.txt
├── scripts
│   └── mlproject-run
├── setup.py
└── tests
    ├── __init__.py
    └── lib_test.py
```

Install package and start using your new function from anywhere you want:
```bash
make install
```
In any notebook:
```python
from mlproject.distance import haversine
```

## Your own script now
The objective here is to implement a new script under `scripts/` called mlproject-computedist taking as parameter 4 coordinates points as input and returning haversine distance.

Install termcolor to allow your script to output colored text `pip install termcolor`.

You can inspect code from `mlproject-computedist` file to understand how to give arguments to a script
Run :
```bash
python computedist.py --coords 48.865 2.380 48.235 2.393
```
Basically you'll want to run the exact same command but without `python` and anywhere on your laptop.
For that simply:
- Create `scripts/mlproject-computedist` file with the exact same code as in `computedist.py`  
👉 __no `.py` at the end of scripts__  
- Add the following lines at the beginning of the file. The first line specifies that the file is a python script. The second line specifies that the file is encoded using UTF-8 characters.
``` python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```
- Modify `setup.py` in order to add `mlproject-computedist` to the list of scripts

Your new tree should look like:
```bash
├── MANIFEST.in
├── Makefile
├── README.md
├── mlproject
│   ├── __init__.py
│   ├── data
│   │   └── data.csv.gz
│   ├── distance.py
│   └── lib.py
├── requirements.txt
├── scripts
│   ├── mlproject-computedist
│   └── mlproject-run
├── setup.py
└── tests
    ├── __init__.py
    └── lib_test.py
```
And your `setup.py` slightly modified:
```python
from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='mlproject',
      version="1.0",
      description="Project Description",
      packages=find_packages(),
      test_suite = 'tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      scripts=['scripts/mlproject-run', 'scripts/mlproject-computedist'],
      zip_safe=False)
```

Finally install package and scripts:
```python
make install
```
And test your script
```bash
mlproject-computedist --help
```
```bash
mlproject-computedist --coords 48.865070 2.380009 48.235070 2.393409
```
To go further on parsing arguments, check [that link](https://www.sicara.ai/blog/2018-12-18-perfect-command-line-interfaces-python)
