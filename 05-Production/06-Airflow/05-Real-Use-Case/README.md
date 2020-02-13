## Objective

Now Let us imagine IKEA offers a service for moving fourniture out.
We want to predict the price of such rides. 

Now let us take a step back and check what we've done so far.
We have implemented:

- A Training DAG that launches, on **_AI Platform**_, training jobs every day on our BQ Table containing both weather and raw data 
- A DAG that gathers weather data every day and store it inside a BQ Table

Additionally, let us imagine that we have every day, fresh new raw data uploaded every night into a Storage Bucket, with the rides of the day.

We might want to:
1°) Enrich our training data with the daily gathered data, both raw and weather data (basically a new DAG to create)
2°) Let our Training DAG launch the daily training on enriched training data (nothing to do here, nice right ?)
3°) Use every day our newly trained model to predict price of a new ride

## Implementation

1°) Implement a DAG that will, at 12:30 am every day
- load gs://daily_rides/20191106.csv data
- merge it with weather from `weather_crawling` table
- insert these into `train_weather_ny_history` table

2°) Sit and relax, no need implement anything
3°) Create a version linked to the model (use tools from lats days):
- use predictor.py from yesterday query data from `weather_crawling` in order add weather data to the instances you want predictions from 