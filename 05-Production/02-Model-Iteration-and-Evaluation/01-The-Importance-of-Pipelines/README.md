# Objective

Yesterday we deployed a model to the GCP, storing it in a joblib object. Given raw data, we could run a preprocessing step on our laptops, build inputs, and make predictions calling the model. Now, we want our saved model `model.joblib` to contain not only the model but also the _**preprocessing**_. To do so, you will create your first scikit-learn pipeline.  

No GCP here, everything on your laptop.

## First simple pipeline

- Open `trainer/task.py `file.
- Complete class `Preprocessing()` with preprocessing function from yesterday's challenge.
- Inspect `sklearn.pipeline.Imputer()` class, what does it do ? Feel free to check sklearn doc here
- Create you First pipeline using `Preprocessing() ` `Imputer()` and the training of your model
- Read function `perf_eval_regression() `from `trainer/tools.py` and test your first pipeline:

```
python -m trainer.task
```

## Pipeline with dependencies

Now let us structure our code for clarity purpose, and for future use

We'll move every Pipeline bloc in a separate python file:
- Create a new a file `trainer/pipeline_blocs.py`, and move `Processing()` from `task.py` to `pipeline_blocs.py`.
- Import it into `trainer/task.py` and run it again to check import.

Inspect function `save_pipeline()`: 
- when would we use it ?
- if we run the Pipeline locally do we need it to do anything ? 
- When will we need to fill it ? 

## Useful documentation for this exercise
Example of custom pre-processing & feature engineering [here](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html#sphx-glr-auto-examples-compose-plot-column-transformer-py). For our processing classes, the transformations will be applied in the `transform` method.
