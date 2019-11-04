# Objective

Implement usefull preprocessing and integrate it into you Pipeline 

## Features Engineering at least

In this challenge, feel free to open a jupyter notebook to inspect the shape of you intermediate dataframes to make your pipeline steps are correct. (use `fit_transform` for each individual transformer to check the transformed data is what you expect).

Here are some features you can add:
- day of week, hour of day, month, year (be careful to the timezone)
- distances, start with [Haversine distance first](https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points)
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
python -m trainer.task.py
```

Better right ?

## To go further

Try and implement Geohash features for pickup and dropoff geolocation

Try and implement Manhattan Distance as a new `ManhatanDistance()`class inside `pipeline_blocs.py`
Help [here](https://dataaspirant.com/2015/04/11/five-most-popular-similarity-measures-implementation-in-python/)  


To make the training faster it is often recommended to scale your features. For this, you can add a scaler transformer. see https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html