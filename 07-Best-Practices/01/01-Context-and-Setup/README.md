### Objectives of the week

1. Bringing all concepts you learned together
1. Work on a real open ended problem
1. Provide guided steps ahead of next week project

We will analyze a dataset provided by e-commerce marketplace [Olist](https://www.olist.com).

### About Olist 🇧🇷

<img src="https://raw.githubusercontent.com/lewagon/data-images/master/best-practices/olist.png" width="500"/>

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

The dataset consists of 9 csv files that can be downloaded on [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce).

You have access to information (customer, seller, product, reviews..) of 100k orders from 2016 and 2018 that were made on Olist store.

More information can be found on [Olist dataset documentation](https://github.com/lewagon/data-challenges/tree/master/07-Best-Practices/data) or on the original Kaggle page.


### Setup

**1 - Collaborate by team on a single repo** ⚠️⚠️

Reminder: you will collaborate by project team on a repo organized as follows

```bash
.
├── data                                 # contains all csv data (not comitted)
|   ├── csv
|       ├── olist_customers_dataset.csv
|       ├── olist_orders_dataset.csv
├── olist                                # contains all scripts contained in Python classes (comitted)
|   ├── order.py
|   ├── product.py
|   ├── seller.py
|   └── utils.py
├── notebooks                            # contains your personal notebooks (not comitted)
|   ├── 01_02_training_set.ipynb
|   └── 01_03_metric_design.ipynb
    └── 02_01_metric_design.ipynb
```

- Project team lead (<user.team_lead_github_nickname>) **and only him** should fork the [olist template](https://github.com/lewagon/olist) repository to its own github account using the github web interface, and invite its team members to collaborate on the forked repo (setting-->manage access-->invite collaborators). Collaborators should recieve an email for confirmation.

- Each team member should then clone the forked repo in its local machine, and copy all challenges needed of the day in their local machine:

```bash
mkdir -p ~/code/<user.team_lead_github_nickname> && cd $_
git clone git@github.com:<team_lead_github_nickname>/olist.git
cd olist
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/01/02-Data-Cleaning/data_cleaning.ipynb notebooks/01_02_data_cleaning.ipynb
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/01/03-Metric-Design/metric_design.ipynb notebooks/01_03_metric_design.ipynb
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/olist/data.py olist/data.py
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/olist/README.md olist/README.md
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/data/README.md data/README.md
```

- Each team member should now create a branch to start working locally on its olist folder without conflicting with other team members.

```bash
git checkout -b <user.github_nickname>-01
```

- Today, each team member will work on all exercices independently. At the end of the day, **one** of your team member should submit a pull request to upload one working version of the code in your shared repo online

```bash
git add olist/data.py
git commit 'a message'
git push -u origin <user.github_nickname>-01
```
- That way, each morning this week, you will be able to resynchronize your code base by pulling the remote master branch

- Notebooks are ignored by git (see `.gitignore`) and will never be uploaded on your shared repo. You may want to collaborate on your findings & graphs throughout the week, in order to prepare for Friday's team presentation. Feel free to create a shared google doc/slide, or create a shared jupyter notebook that you can force to commit by using `git add -force <your_shared_notebook.ipynb>`

**2 - Edit your PYTHONPATH**

- Add `olist` path to your `PYTHONPATH`. This will help us easily import our modules throughout the class.

On Mac and Linux:

_Open a terminal and run this._
```bash
cd ~/code/<user.team_lead_github_nickname/olist && echo "export PYTHONPATH=\"$(pwd):\$PYTHONPATH\""
```
_Then copy the output line into your ~/.zshrc file by using st ~/.zshrc to open this config file as usual)_

_Restart your terminal for the new .zshrc file to be loaded_


For Windows:

- `System Properties > Advanced> Environment Variables.`
- Locate the Variable name `PYTHONPATH`
- Add your path `C:\path\to\olist`
