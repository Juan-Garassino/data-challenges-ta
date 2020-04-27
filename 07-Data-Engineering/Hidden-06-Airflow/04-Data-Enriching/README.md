## Objective

The objective here is to run a worklow gathering data from external source.

We will use a weather API to gather only one weather data information every day

## Weather API 

Create a free account on this [Weather API](https://www.worldweatheronline.com/developer/api/docs/historical-weather-api.aspx#qparameter)  
No card needed for account creation

Get your ApiKey

Implement `weather_api()` class inside api_insert aiming at connecting to the API, and getting current day's weather data (only one point)

Now implement `load_bq_table_from_df()` to load api result into a new BQ table named `weather_crawling`

Test your 2 functions by requesting data from the whole 2018 year and inserting it into our table.  

## Dag implementation

Create dag_weather_api.py file and implement a dag that will insert into `weather_crawling` table, **_every day at 1 am_**,  the weather's forecast data information (only one)

Only keep `date`, `mintempF`, `maxtempF`, and `totalSnow_cm` fields from the api response  

Rename those 1 fields after the corresponding fields names of you training Table, because you will insert data from `weather_crawling` table into your training table in next exercices.

