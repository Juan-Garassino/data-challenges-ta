# Objective

In this step, you will implement useful preprocessing and integrate it into you Pipeline. You can store these preprocessing steps in your `pipeline_blocs.py` file, this will help you have a clear code organization. You can then call these blocs from your `task.py` script.

## Features Engineering at least

In this challenge, feel free to open a jupyter notebook to test your code and inspect the shape of your intermediate dataframes to make sure that your pipeline steps are correct (use `fit_transform` for each individual transformer to check the transformed data is what you expect).

Here are some features you can add:
- day of week, hour of day, month, year (be careful to the timezone)
- distance between start and end of the taxi trip (Euclidian, Haversine, Manhattan)
- flag indicating whether drop off location is airport  
- geohashes

## Integrate Feature Engineering into your Pipeline

Now from Notebook to `pipeline_blocs.py`:
- Fill in `TimeFeatures() `and `DistanceFeature() `classes 
- Understand how these classes work, what is the output of :
```bash
df1 = pd.read_csv(PATH_TO_FILE)
TimeFeatures(time_column="pickup_datetime").fit_transform(df1)
```
- Understand the need for `FeatureUnion() `class in `trainer/task.py `

## Fit and evaluate pipeline

Run your pipeline:
```bash
python -m trainer.task
```

Better right ?

## Useful documentation for this exercise
Example of custom pre-processing & feature engineering [here](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html#sphx-glr-auto-examples-compose-plot-column-transformer-py). For our processing classes, the transformations will be applied in the `transform` method.

## To go further
To make the training faster it is often recommended to scale your features. For this, you can add a [scaler transformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html).
