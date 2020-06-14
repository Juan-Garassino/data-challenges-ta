# From Notebook to package

It is time to move away from Jupyter Notebook, and start writing reusable code with python packages, modules and classes.

In the exercice, nothing new, simply copy pasting functions we already implemented yesterday, and organize them inside different modules.

Let's first create our folder structure, we did the following steps for you:

1. Create a folder with the name of your project/package, for example `TaxiFareModel`
2. Inside this folder, create a `__init__.py` file to make it a python package
3. Then create multiple python files (modules) that will contain the different python classes or methods we need

* `trainer.py`: **Trainer** class that will be our main class that trains our model
* `data.py`: **Data** functions to get and clean data
* `utils.py`: any utility functions you may have
* `encoders.py`: your custom encoders and transformers for our Pipeline

You should have something like:

* TaxiFareModel
    * __init__.py
    * data.py
    * encoders.py
    * trainer.py
    * utils.py

This exercice loads the train data from an Amazon AWS S3 bucket, in order to access it
- `pip install s3fs`

#### data.py
- Inspect functions `get_data` and `clean_df` that are already given to you.

NB: Here we provide you with the same functions so that we all get and clean data the same way.

#### utils.py
- In `utils.py` this is where you can have :
 - `haversine_distance` method
 - `compute_rmse` method

#### encoders.py
- In `encoders.py` let's put the custom encoders and transformers you have for distance and time features

##### Reminder
Let us be clear about the use of `encoders.py` here:
- It contains all custom pipeline preprocessing blocs not provided by sklearn
- The way to implement such blocks has been seen on yesterday's exercices

#### trainer.py

Implement the main class here
- The `Trainer` class is the main class. It should have:
  - a `def __init__()` method instanciating class
  - a `def get_estimator()` to return the estimator chosen to train the model
  - a `def set_pipeline()` method that builds the pipeline
  - a `def train()` method that trains the pipeline
  - a `def evaluate()` method evaluating model

- Make sure you are confident with following notions
 - attributes and methods of a class
 - `**kwargs` argument of a function and how to use it, (help [HERE](https://www.programiz.com/python-programming/args-and-kwargs) if unclear)
 - use of `__init__(self, **kwargs)` method

```python
class Trainer(object):

    def __init__(self, X, y, **kwargs):
        self.pipeline = None
        self.X_train = X
        self.split = kwargs.get("split", True)
        ...
        self.y_train = y

    def get_estimator(self):
        """return estimator"""

    def set_pipeline(self):
        """define pipeline here, define it as a class attribute"""

    def evaluate(self, X_test, y_test):
        """evaluates the pipeline on df_test"""

    def train(self):
        pass
```

### Test it!
- Once you have everything setup, test that it works by running :
```
python -m TaxiFareModel.trainer
```
Or
```bash
python -i TaxiFareModel/trainer.py
```

## Hints for debugging
- Do not hesitate to only breakdown your code into smaller calls for debugging
- Use [if \_\_name__ == '\_\_main__'](http://sametmax.com/pourquoi-if-__name__-__main__-en-python/) at the end of each `.py` file to debug
- For instance to debug data.py, add at the end:
```python
if __name__ == '__main__':
    df = get_data()
```
And then install and run `ipython` inside terminal:
```bash
pip install ipython
ipython
```
```
Python 3.7.2 (default, Feb 20 2020, 16:34:30)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.12.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: %run TaxiFareModel/data.py

In [2]: df.shape
```
