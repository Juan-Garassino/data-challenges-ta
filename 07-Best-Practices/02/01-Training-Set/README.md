### Setup

- let's start by copying the exercies of the day to your local olist folder

```bash
cd ~/code/<user.team_lead_github_nickname>/olist
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/02/01-Training-Set/training_set.ipynb notebooks/02_01_training_set.ipynb
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/02/02-Multivariate-Regression/multivariate_regression.ipynb notebooks/02_02_multivariate_regression.ipynb
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/02/03-Reviews-Translator/review_translator.ipynb notebooks/02_03_review_translator.ipynb
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/olist/order.py olist/order.py
```
- Make sure everyone on your team starts with the same comitted code base, and create your own branch for the day 2

```bash
git checkout master
git pull origin master --rebase
git checkout -b <user.github_nickname>-02
```

- At the end of the day, don't forget to push one working version of your code to your team repo, and (optionally) to summarize your key findings in your team google doc or shared notebook.

#### Exercice: Training Set 🏋️‍

Today, we will investigate the **orders**, and their associated review score.

For that purpose, we will create one single data table containing all orders as index and all properties of these orders as columns.

As you may have noticed, information is scattered between the various olist data tables. Therefore, we will code in the `olist/order.py`file all logic needed to return a training set at the order level. This will come handy for our next modeling phase.

- Open `notebooks/02_01_training_set.ipynb` and follows instructions
- The `olist/order.py` solution will be given to the class by 2pm to make sure you are able to move to the next exercice on time
