### Objectives of the week

1. Bringing all concepts you learned together
1. Work on a real open ended problem
1. Provide guided steps ahead of next week project

We will analyze datasets provided by e-commerce marketplace [Olist](www.olist.com).

### About Olist 🇧🇷

![olist](https://raw.githubusercontent.com/lewagon/data-images/master/best-practices/olist.png)

Olist is a leading e-commerce service that connects merchants to main marketplaces in Brazil. They provide a wide range of offers from inventory management, dealing with reviews and customer contacts to logistic services.

Olist charge sellers a monthly fee. This fee is progressive with the volume of orders.

Remember the seller and customer workflows:

**Seller:**
- Seller join Olist
- Seller upload product catalogue
- Seller get notified when a product is sold.
- Seller hand over item to logistic carrier.

👉 Note that multiple sellers can be involved in one customer order!

**Customer:**
- Browse products on marketplaces
- Purchase products from Olist.store
- Get an expected date for delivery
- Customer Receive order
- Customer leave a review for the order

👉 A review can be left as soon as the order is sent, meaning that a customer can leave a review for a product he did not receive yet!

### Dataset

The dataset consists of 8 csv files that can be downloaded on [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce).

You have access to information (customer, seller, product, reviews..) of 100k orders from 2016 and 2018 that were made on Olist store.

More information can be found on [Olist dataset documentation](https://github.com/lewagon/data-challenges/tree/master/07-Best-Practices/data) or on the original Kaggle page.


### Setup

To get started, make sure you install the needed python packages by running:

```bash
pip install -r ../../requirements-best_practices.txt
```
