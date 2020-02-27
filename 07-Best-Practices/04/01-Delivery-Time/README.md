## Setup

Make sure everyone on your team starts with the same comitted code base, and create your own branch for the day 4:

```bash
cd ~/code/<user.team_lead_github_nickname>/olist
git status # Check that you're repo is clean. If not, ask a TA
git checkout master
git pull origin master
git checkout -b <user.github_nickname>-04
```

Then, copy the exercies of the day to your local olist folder

```bash
cd ~/code/<user.team_lead_github_nickname>/olist
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/04/01-Delivery-Time/delivery_time.ipynb notebooks/04_01_delivery_time.ipynb
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/04/02-Review-Classification/review_classification.ipynb notebooks/04_02_review_classification.ipynb
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/04/03-Text-Classification/text_classification.ipynb notebooks/04_03_text_classification.ipynb
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/olist/review.py olist/review.py
```

- At the end of the day, don't forget to push one working version of your code to your team repo, and (optionally) to summarize your key findings in your team google doc or shared notebook.


## Delivery Time

Estimated Time Arrival (ETA) is a key component of modern e-commerce services. It allows to manage customer expectations by displaying a predicted date for customer delivery.

In this section, we will improve Olist ETA predictions and build a predictive model that will outperform the current version.

Olist current model is shown in column `order_estimated_delivery_date` in the order dataset.

Our variable to optimize is `wait_time`: the difference in days between the actual delivery date (`order_delivered_customer_date`) and the date of the order purchase (`order_purchase_timestamp`).

### Baseline

We first need to understand the baseline we want to optimize.

- Plot `wait_time` and `expected_wait_time` distribution. What's the median difference ?
- What's the `RMSE` for Olist's current ETA model?

### First Model

Load orders training data and split it with a 30% test size in X_train, X_test, y_train, y_test.

👉 Hint: make sure to drop the necessary variables to avoid data leakage.

Build a first prediction with the model of your choice. What’s the best wait_time you get?

### More Features

We did a first pass at improving Olist ETA. Can we do better using additional features?

- Create additional columns that correspond to the product category features at the order_id level. Does that increase the `RMSE` of your model?

### Auto ML

Using the library [Tpot](http://epistasislab.github.io/tpot/), find the best model to optimize `wait_time`. What is the best `mean_square_error` you can achieve?
