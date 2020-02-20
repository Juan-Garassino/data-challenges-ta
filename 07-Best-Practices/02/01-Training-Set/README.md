### Setup

let's start by copying the exercies of the day to your local olist folder

```bash
cd ~/code/<user.github_nickname>
mkidr ~/code/<user.github_nickname>/olist/notebooks/02/01-Training-Set
mkidr ~/code/<user.github_nickname>/olist/notebooks/02/02-Multivariate-Regression
mkidr ~/code/<user.github_nickname>/olist/notebooks/02/03-Reviews-Translator
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/02/01/training_set.ipynb ~/code/<user.github_nickname>/olist/notebooks/02/01/training_set.ipynb
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/02/02/multivariate_regression.ipynb ~/code/<user.github_nickname>/olist/notebooks/02/02/multivariate_regression.ipynb
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/02/03/review_translator.ipynb ~/code/<user.github_nickname>/olist/notebooks/02/03/review_translator.ipynb
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/olist/order.py ~/code/<user.github_nickname>/olist/olist/order.py
```

- Pull the master branch of your team repo to make sure everyone on your team starts with the same comitted code base, and create your own branch for the day

```bash
cd ~/code/<user.github_nickname>/olist
git checkout master
git pull origin master --rebase
git checkout -b <user.github_nickname>-02
```


- At the end of the day, don't forget to push one working version of your code to your team repo, and (optionally) to summarize your key findings in your team google doc or shared notebook.

#### Exercice: Training Set 🏋️‍
In this challenge, we will implement a method to return a training set at the order level. We will implement this training set in the `olist/order.py` file. This will come handy for our next modeling phase.

- Open `notebook/02/01/training_set.ipynb` and follows instructions
