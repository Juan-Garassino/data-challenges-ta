### Objectives of the week

1. Bringing all concepts you learned together
1. Work on a real open ended problem
1. Provide guided steps ahead of next week project

We will analyze a dataset provided by e-commerce marketplace [Olist](www.olist.com).

### About Olist 🇧🇷

![olist](https://raw.githubusercontent.com/lewagon/data-images/master/best-practices/olist.png)

Olist is a leading e-commerce service that connects merchants to main marketplaces in Brazil. They provide a wide range of offers from inventory management, dealing with reviews and customer contacts to logistic services.

Olist charges sellers a monthly fee. This fee is progressive with the volume of orders.

Remember the seller and customer workflows:

**Seller:**
- Seller join Olist
- Seller upload product catalogue
- Seller get notified when a product is sold.
- Seller hand over item to logistic carrier.

👉 Note that multiple sellers can be involved in one customer order!

**Customer:**
- Browses products on marketplaces
- Purchases products from Olist.store
- Gets an expected date for delivery
- Customer receives the order
- Customer leaves a review about the order

👉 A review can be left as soon as the order is sent, meaning that a customer can leave a review for a product he did not receive yet!

### Dataset

The dataset consists of 8 csv files that can be downloaded on [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce).

You have access to information (customer, seller, product, reviews..) of 100k orders from 2016 and 2018 that were made on Olist store.

More information can be found on [Olist dataset documentation](https://github.com/lewagon/data-challenges/tree/master/07-Best-Practices/data) or on the original Kaggle page.


### Setup

**1 - Edit your PYTHONPATH**

- Add `07-Best-Practices` path to your `PYTHONPATH`. This will help us easily import our modules throughout the class. 

On Mac:

```bash
open ~/.zshrc
export PYTHONPATH="/Users/username/repos/data-challenges/07-Best-Practices:$PYTHONPATH"
```

⚠️ Make sure to replace `username` with your local username.

For Windows: 

- `System Properties > Advanced> Environment Variables.`
- Locate the Variable name `PYTHONPATH`
- Add your path `C:\path\to\07-Best-Practices` 

**2 - Install required packages**

- Install needed python packages with the command: 

```python
pip install -r requirements-best_practices.txt
```