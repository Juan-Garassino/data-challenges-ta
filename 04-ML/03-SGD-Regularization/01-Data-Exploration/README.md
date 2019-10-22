# Introduction

Today, you will learn to recode entirely a linear regression algorithm. Linear regression can be solved using the *normal equation* (closed-form solution) or, as we will do today, with gradient descent (which can be faster when there are a lot of features in the dataset).

Here are the steps we will implement:

- 1. Start with some random parameter values: we call this *random initialization*. *Zero initialization* is also possible.
- 2. Calculate the output of the algorithm with these parameters: this is the equivalent of *forward propagation* with neural networks.
- 3. Calculate the error with these parameters: we compare the output of the algorithm with the ground truth (this is a supervised algorithm so we need the ground truth).
- 4. Evaluate how to change each parameter to reduce the error and update the parameters: this is the equivalent of *backward propagation* with neural networks and gradient descent is the core of this step.

For these exercises, we'll use the [Ciqual dataset](https://ciqual.anses.fr/#) showing the composition of food.🌽

# First exercise

In this introductory exercise you will explore the Ciqual dataset that we will use along the day. You can start by opening the notebook `01-Data-Exploration.ipynb`.
