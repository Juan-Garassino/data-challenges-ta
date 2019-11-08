## 07-Best-Practices

Welcome to week 7 of LeWagon Data Bootcamp 🎉

Goals of this week: 
1. Bringing all concepts you learned together
2. Work on a real open ended problem
3. Provide guided steps ahead of next week project

We will analyze a dataset provided by e-commerce marketplace [Olist](www.olist.com). 

### About Olist 🇧🇷

<img src='img/olist.png' width='700'>

Olist is a leading e-commerce service that connect merchants to main marketplaces in Brazil. They provide a wide range of offers from inventory management, dealing with reviews and customer contacts to logistic services.
Olist charge sellers a monthly fee. This fee is progressive with volume of orders. 

Remember the seller and customer workflows: 

Seller: 
  - Seller join Olist
  - Seller upload product catalogue
  - Seller get notified when a product is sold.
  - Seller hand over item to logistic carrier.
  👉 Note that multiple sellers can be involved in one customer order!

Customer: 
  - Browse products on marketplaces
  - Purchase products from Olist.store
  - Get an expected date for delivery
  - Customer Receive order
  - Customer leave a review for the order
  👉A review can be left as soon as the order is sent, meaning that a customer can leave a review for a product he did not receive yet!

### Dataset 

The dataset consists of 8 csv files that can be downloaded on [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce). 

You have access to information (customer, seller, product, reviews..) of 100k orders from 2016 and 2018 that were made on Olist store.

More information can be found on [Olist dataset documentation](https://github.com/lewagon/data-challenges/tree/master/07-Best-Practices/data) or on the original Kaggle page. 

### Setup

To get started, make sure to complete the two steps below:

**1 - Edit your PYTHONPATH**

- Add `07-Best-Practices` path to your `PYTHONPATH`. This will help us easily import our modules throughout the class. 

On Mac:

```bash
open ~/.bashrc
export PYTHONPATH="/Users/username/repos/data-challenges/07-Best-Practices:$PYTHONPATH"
```

For Windows: 

- `System Properties > Advanced> Environment Variables.`
- Locate the Variable name `PYTHONPATH`
- Add your path `C:\path\to\07-Best-Practices` 

**2 - Install required packages**

- Install needed python packages with the command: 

```python
pip install -r requirements-best_practices.txt
```