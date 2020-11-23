
## Build a docker image for our API

We now have a working prediction API. Let's create a container image for our prediction API and use it locally.

Let's start by creating the `Dockerfile` that will contain the instructions telling Docker how to build the image.

### FROM directive

Search for a base image in [Docker Hub](https://hub.docker.com/) which would contain a suitable version of python.

👉 [List of Docker Hub available python images](https://hub.docker.com/_/python)

Use the base image in order to create the `Dockerfile`.

``` Dockerfile
FROM python:3.8.6-buster
```

We have built a `Dockerfile` able to create an image based on a Linux distribution and that is able to run python code.

### COPY directives

We want to add our code to the image, so that the image can run the code.

Let's add instructions to tell docker to copy in the image:
- the trained model
- the code of the project which is required in order to load the model
- the code of our API
- the list of requirements

``` Dockerfile
FROM python:3.8.6-buster

COPY api /api
COPY project /project
COPY model.joblib /model.joblib
COPY requirements.txt /requirements.txt
```

We are now able to build an image able to run our code, but what about the dependencies of our code? 🤔

### RUN directive

We need to tell docker to install the dependencies of our code when the image is built.

Let's use a RUN directive in order to ask docker to install the python packages required by our image.

``` Dockerfile
FROM python:3.8.6-buster

COPY api /api
COPY project /project
COPY model.joblib /model.joblib
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt
```

Looks like we are almost finished: our `Dockerfile` now enables use to build an image:
- based on a linux distribution
- running python code
- where our code is copied
- and the dependencies of our code are installed

### CMD directive

We now need to tell docker what the image should do when it is started. Otherwise we will only have started an image with our code and its dependencies, and that actually does nothing.

Hint: we need to provide the following `host` and `port` parameters to the `Flask` command.
The `host` parameter will tell flask to listen to all network connections.
The `port` parameter will tell flask to listen to HTTP requets on the $PORT configured by the cloud service running our docker image.

If we fail to provide any of these parameters, our image will run but the flask server will be unable to receive incoming http requests.

``` Dockerfile
FROM python:3.8.6-buster

COPY api /api
COPY project /project
COPY model.joblib /model.joblib
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

CMD env FLASK_APP=api.flask flask run --host 0.0.0.0 --port $PORT
```

## Make sure the docker image works on our machine

Now let's build the image! ⏰

``` bash
docker build --tag=taxifare-pred-api .
```

Once built, the image should be visible in the list of images:

```
docker images
```

Let's run it 👌

Remember since we configured the image with a $PORT environment variable, we need to provide it now.

We also need to specify the mapping between the port inside of the image and the port at which we will contact the image.

``` bash
docker run -e PORT=8000 -p 8000:8000 taxifare-pred-api
```

Let's look at the status of the image.

``` bash
docker ps
```

You can now go to [the main page](http://localhost:8000/) of the Flask server and see a magnificent "Hello, World!".

Let's play with the API an receive your first prediction!

``` python
import requests

params = dict(
  key='2012-10-06 12:10:20.0000001',
  pickup_datetime='2012-10-06 12:10:20 UTC',
  pickup_longitude=40.7614327,
  pickup_latitude=-73.9798156,
  dropoff_longitude=40.6413111,
  dropoff_latitude=-73.7803331,
  passenger_count=2
)

taxifare_api_url = "http://127.0.0.1:8000/predict_fare"

response = requests.get(
    taxifare_api_url,
    params=params,
).json()

print(response)
```

It's Alive! 😱 🎉

You may stop (or kill) the image...

``` bash
docker stop 152e5b79177b  # ⚠️ use the correct CONTAINER ID
docker kill 152e5b79177b  # ☢️ only if the image refuses to stop (did someone create an ∞ loop?)
```
