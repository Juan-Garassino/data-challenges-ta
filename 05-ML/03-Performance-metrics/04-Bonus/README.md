# Bonus

## Download the dataset

The dataset is available [here](https://wagon-public-datasets.s3.amazonaws.com/Machine%20Learning%20Datasets/ML_creditcard_fraud.csv)). Let's download it and store it in the `data` folder in the `04-Bonus` directory with the following commands:

```bash
cd ~/code/<user.github_nickname>/data-challenges/05-ML/03-Performance-metrics/04-Bonus
curl https://wagon-public-datasets.s3.amazonaws.com/Machine%20Learning%20Datasets/ML_Creditcard_fraud.csv > data/creditcard.csv
```

## The dataset

The datasets contains transactions made by credit cards. Due to confidentiality issues, the original features have been preprocessed and renamed V1 to V28. There are two features which have not been transformed: `Time` and `Amount`. Feature Time contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature Amount is the transaction Amount. `Class` is the target and it takes value 1 in case of fraud and 0 otherwise.

## Exercice

🎯 You are a Data Scientist for a bank. You are asked to develop a model that is able to detect at least 95% of fraudlent transactions. Go!

To start the exercise, open `Bonus.ipynb` in `jupyter notebook` and follow the instructions.

🚀 Your turn!


