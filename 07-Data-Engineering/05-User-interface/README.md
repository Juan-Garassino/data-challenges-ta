
# Let's create another website project

Let's create a new project for our website! 🔥

Create a new project `TaxiFareWebsite` in your working directory:

```bash
cd ~/code/<user.github_nickname>
mkdir TaxiFareWebsite
cd TaxiFareWebsite
```

Initialise a new git repository:

```bash
git init
```

Create a corresponding repository on your **GitHub** account:
``` bash
gh repo create
```

Go to the GitHub repo:

``` bash
gh repo view --web
```

Change the visibility to private (in the settings of the repository)...

You are now all set!

# User interface

Yesterday, we have put in production our **Prediction API** on **Google Cloud Run**.

This interface allows any developers in the world 🌍 to user our API in order to predict the fare amount of a taxi ride in New York.

Today, we want to expand our user to the global population.

👉 We need to provide an interface that anyone can use without any prior knowledge of computer science.

Let's create our first web site.

Our web site will allow users to predict a fare 🔥

First, we will see how to plug an existing website to our API.

Then, we will create our own website using **Streamlit**
