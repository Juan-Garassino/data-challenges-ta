## Setup

Make sure everyone on your team starts with the same comitted code base, and create your own branch for the day 3:

```bash
cd ~/code/<user.team_lead_github_nickname>/olist
git status # Check that you're repo is clean. If not, ask a TA
git checkout master
git pull origin master
git checkout -b <user.github_nickname>-03
```

Then, copy the exercies of the day to your local olist folder

```bash
cd ~/code/<user.team_lead_github_nickname>/olist
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/03/01-Logit-Orders/03_01_logit_orders.ipynb notebooks/03_01_logit_orders.ipynb
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/03/02-Product-Categories/product_impact.ipynb notebooks/03_02_product_impact.ipynb
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/03/03-Seller-Performance/Sellers.ipynb notebooks/03_03_seller_performance.ipynb
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/olist/product.py olist/product.py
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/olist/seller.py olist/seller.py

```

- At the end of the day, don't forget to push one working version of your code to your team repo, and (optionally) to summarize your key findings in your team google doc or shared notebook.


## Exercice 1: Model orders reviews with logistic regression

In this section we want to understand, using a logistic regression this time, which variables correlate to either 1 star reviews or 5 stars reviews.

Open the `03_01_logit_orders.ipynb` and follow instructions (copied below)

**One Star**
- Run a logistic regression to predict `dim_is_one_star` on the explaning variables of your choice.
- Which variables have higher impact on dim_is_one_star reviews?
- How do you interpret results?

**Five Star**
- Run a logistic regression to predict `dim_is_five_star` on the explaning variables of your choice.
- Which variables have higher impact on dim_is_one_star reviews?
- Do you notive differences with One Star?
- How do you interpret results?
