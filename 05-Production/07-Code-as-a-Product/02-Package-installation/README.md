## Objective 

Install your `mlproject` package

## Inspect code

The purpose of `mlproject` are:
- install it as a module
- install scripts 

Get inside `mlproject`  
Inspect script under `scripts/mlproject-run`  
Inspect code you want to package as a module under `mlproject/`

You'll want to install these dependencies and the script.  

First in install python requirements specific to this project, then install package.

```bash
make install_requirement
```

```bash
make install
```

## Project as a module
Your mlproject is now a module, just like pandas or sklearn

Go anywhere you want and launch inside ipython:

```
from mlproject.lib import clean_data
```

Same for Notebooks
## Python as scripts

You also have installed a script, test it:
```
mlproject-run
```

## Your own script now

Implement a new script under `scripts/` called mlproject-commputedis taking as parameter 4 coordinates points as input and returning haversone distance.

You'll want to use [argparse](https://docs.python.org/2/library/argparse.html) module here

To go further on parsing arguments, check [that link](https://www.sicara.ai/blog/2018-12-18-perfect-command-line-interfaces-python)

