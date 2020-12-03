
In the previous challenges, we created a project containing the code allowing us to:
- **Train our model** at scale
- Deploy our **Prediction API** on **Google Cloud Run**

We now have a live API allowing developers all over the world to predict the fare amount for a taxi ride in New-York 🎉

👉 Optionally, we may start from the correction of the `07-Data-Engineering/04-Predict-in-production/03-GCR-cloud-run` exercice 👌

Now, we want to allow users all over the internet to be able to use our model in order to make a fare amount prediction, not just developers.

In order to do that, we are going to create a website allowing regular users to interact with our model.

Let's add a **Front-End** (website) on top of our **API** in order to visualize our predictions.

# First, let's create a new project

For now, all the code that we have been using for data exploration (notebooks), model training and building our prediction API in contained in a single project.

We are going to create a new project for our website.

🤔 Why would we want to split our code into 2 projects ? Separating the model training + prediction API from the website will allow the package for the website to be very light.

Actually, the package for our website will not require to contain any Data Science related code, since the website will be using our own API in order to make predictions.

Splitting the code between training/prediction and website has several benefits:
- We will be able to deploy our small package on light hosting solutions such as **GitHub Pages** and **Heroku**, which can operate for free 💵
- Splitting the complexity will allow other team of developers (for example web developers) to work with us without requiring any Data Science related knowledge
- It follows to popular web development pattern of separating the **Front-End** code (the website) from the **Back-End** code (the service), both communicating through an **API**

In this exercice, we are going clone a repository containing an existing TaxiFare website and modify it in order to plug it to our **Prediction API**.

This will give we an overview of what can be done in order to expose an API.

This website will be contained inside its own project.

In the next exercice, we will code our own website from scratch with Streamlit 🎉 And this second website will also have a project of its own...

# Let's go!

Let's use the [Le Wagon homemade TaxiFare frontend](https://github.com/lewagon/taxi-fare-interface) repository in order to plug [this Front-End](https://lewagon.github.io/taxi-fare-interface/index.html) to our **Prediction API**.

We will start by creating a duplicate template of this repository on our own GitHub account, by clicking on the `Use this template` button in the page of the repository on GitHub or [using this link](https://github.com/lewagon/taxi-fare-interface/generate).

👉 **VERY IMPORTANT** we need to make our new repository a **PUBLIC REPOSITORY**, otherwise the **GitHub Pages** hosting solution that we want to introduce for this exercice will not work.

👉 Let's name this repository `taxi-fare-interface`.

Now that we have a `taxi-fare-interface` repository on our GitHub account, we can clone it in order to modify it.

Let's go right next to the `data-challenges` directory:

``` bash
cd ~/code/<user.github_nickname>
```

Let's clone our GitHub `taxi-fare-interface` repository:

``` bash
git clone git@github.com:<user.github_nickname>/taxi-fare-interface.git
```

And step inside in order to work on it:

``` bash
cd ~/code/<user.github_nickname>/taxi-fare-interface
```

Now, we will follow the instructions from the [taxi-fare-interface](https://github.com/lewagon/taxi-fare-interface) repository in order to plug our **Prediction API** to the website!

Let's:

👉 Run our Front-End locally.

👉 Deploy our Front-End on **Github Pages**.

*Hint*: alternatively, you may use this Le Wagon **Prediction API** if you you do not have one in production:

https://taxi-fare-api-jbgixi3psq-ew.a.run.app/

https://taxi-fare-api-jbgixi3psq-ew.a.run.app/predict_fare/?key=2012-10-06%2012:10:20.0000001&pickup_datetime=2012-10-06%2012:10:20%20UTC&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2
