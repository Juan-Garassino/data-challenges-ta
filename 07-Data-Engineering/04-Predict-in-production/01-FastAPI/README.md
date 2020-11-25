
## Let's create our first API exposing our model

Yesterday, we trained our TaxiFare model in the cloud using the **AI Platform**.

We saved one or more versions of our model in a `model.joblib` file.

Let's use our best performing model in order to make predictions.

⚠️ Do not forget that we cannot load our model without the code that was used in order to train it! ⚠️

### First step: lets create an entry point and test it

Let's create a root entry point that will welcome the developers using our API.

The entry point will simply return the following json content when a developer hits the root of our API : http://localhost:8000/

``` json
{
  "key": "value"
}
```

*Hint*: you may use the `make run_api` **Makefile** directive in order to run the **uvicorn** web server that will serve the API.

Once the server is started, you can play with the API either directly: http://localhost:8000/

... Or through the **Swagger** documentation: http://localhost:8000/docs (click on the endpoint you wish to play with, and hit `Try it out`)

### Receive the parameters for the prediction

Let's now create a `/predict_fare` entry point that will be used for our predictions.

We want developers to provide the following parameters to the entry point:
- `pickup_datetime`
- `pickup_longitude`
- `pickup_latitude`
- `dropoff_longitude`
- `dropoff_latitude`
- `passenger_count`

As a response, let's send back the provided values in order to make sure that everything is working correctly:

``` json
{
  "pickup_datetime": "2013-07-06 17:18:00 UTC",
  "pickup_longitude": "-73.950655",
  "pickup_latitude": "40.783282",
  "dropoff_longitude": "-73.984365",
  "dropoff_latitude": "40.769802",
  "passenger_count": "1"
}
```

### Predicting the fare amount

Now that the piping is done, let's make an actual prediction.

But first, we need to store the parameters as an observation in an `X_pred` dataframe.

The columns should match the format of the `X_train` having served to train the pipeline of our model.

*Hint*: the code provided for the TaxiFare model uses an additional **key** column. Its value ({ "key": "2013-07-06 17:18:00.000000119" }) will not affect the model, but if the column is missing the pipeline will not accept your dataframe as input...

⚠️ Beware to the order of the columns when you create the dataframe! ⚠️

**Pandas** does not care about the order of the columns, but **Numpy** does, and you might end up surprised by the results if you build a dataframe with an incorrect order of columns...

Now that we have created a `X_pred` dataframe, let's perform a prediction.

Let's load our model, either from **Google Cloud Storage** or from our local hard drive.

We just need to store the resulting prediction in our **json** response:

``` json
{
  "prediction": 1.234
}
```

*Hint*: in order to play with your API, you may either fill the parameters manually in the URL, or use the notebook provided in `notebooks/API usage.ipynb`.

⚠️ The notebook is built to query an API responding to the following URL... Maybe you will want to adapt the way the notebook works if you choose a different format for your API ⚠️

http://127.0.0.1:8000/predict_fare/2012-10-06%2012:10:20.0000001/2012-10-06%2012:10:20%20UTC/40.7614327/-73.9798156/40.6513111/-73.8803331/2

Congratulations, you just created your first API! 🎉

Let's see how we can put this API into production so that it gets exposed to the internet 🚀
