## Objectives of the week

1. Bringing all concepts you learned together
1. Work on a real open ended problem
1. Provide guided steps ahead of next week project

We will analyze a dataset provided by e-commerce marketplace [Olist](https://www.olist.com).

## About Olist 🇧🇷

<img src="https://raw.githubusercontent.com/lewagon/data-images/master/best-practices/olist.png" width="500"/>

Olist is a leading e-commerce service that connects merchants to main marketplaces in Brazil. They provide a wide range of offers from inventory management, dealing with reviews and customer contacts to logistic services.

Olist charges sellers a monthly fee. This fee is progressive with the volume of orders.

Here are the seller and customer workflows:

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

## Dataset

The dataset consists of 9 csv files that can be downloaded on [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce).

You have access to information (customer, seller, product, reviews..) of 100k orders from 2016 and 2018 that were made on Olist store.

More information can be found on [Olist dataset documentation](https://github.com/lewagon/data-challenges/tree/master/07-Best-Practices/data) or on the original Kaggle page.


## Setup

### 1 - Collaborate as a team on a common repository

Reminder, you will collaborate by project team on a repo organized with the following tree structure:

```bash
.
├── data                                 # all csv data (not comitted)
|   └── csv
|       ├── olist_customers_dataset.csv
|       └── olist_orders_dataset.csv
├── olist                                # all scripts contained in Python classes (comitted)
|   ├── order.py
|   ├── product.py
|   ├── seller.py
|   └── utils.py
└── notebooks                            # your *personal* notebooks (not comitted)
    ├── 01_02_training_set.ipynb
    └── 01_03_metric_design.ipynb
    └── 02_01_metric_design.ipynb
```

Pay attention to who does what:

- Project team lead (`<user.team_lead_github_nickname>`) **and only him/her** must use the [olist template](https://github.com/lewagon/olist) repository to create a repository on his/her own github account. (USe this template --> owner: you --> setting private)
- Then project team lead can invite his/her team members to collaborate on the newly created repo (setting-->manage access-->invite collaborators).
- Other team members will recieve an email invitation they need to accept.
- Every team member (including `<user.team_lead_github_nickname>`) must clone the repo on his/her local machine and set it up with the following commands:

```bash
mkdir -p ~/code/<user.team_lead_github_nickname> && cd $_
git clone git@github.com:<user.team_lead_github_nickname>/olist.git && cd olist
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/01/02-Data-Cleaning/data_cleaning.ipynb notebooks/01_02_data_cleaning.ipynb
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/01/03-Metric-Design/metric_design.ipynb notebooks/01_03_metric_design.ipynb
cp ~/code/<user.github_nickname>/data-challenges/07-Best-Practices/olist/data.py olist/data.py
```

Each team member can now create a branch to start working locally on his/her olist folder without conflicting with other team members:

```bash
git checkout -b <user.github_nickname>-01
```

Today, each team member will work on all exercices independently. At the end of the day, **one** of your team member should submit a pull request to upload one working version of the code in your shared repo online

```bash
git add olist/data.py
git commit 'Completed Day 1'
git push -u origin <user.github_nickname>-01
```

That way, each morning this week, you will be able to resynchronize your code base by pulling the remote master branch

Notebooks are ignored by git (see `.gitignore`) and will never be uploaded on your shared repo. You may want to collaborate on your findings & graphs throughout the week, in order to prepare for Friday's team presentation. Feel free to create a shared google doc/slide, or create a shared jupyter notebook that you can force to commit by using `git add -force <your_shared_notebook.ipynb>`

### 2 - Edit the `PYTHONPATH`

Add `olist` path to your `PYTHONPATH`.

This will allow you to easily import modules defined in `olist` in your notebooks throughout the week.

For macOS and Linux, open a terminal and run:

```bash
cd ~/code/<user.team_lead_github_nickname>/olist && echo "export PYTHONPATH=\"$(pwd):\$PYTHONPATH\""
```

Then copy the output line at the bottom of your `~/.zshrc` file. (You can open it with Sublime Text or `vim` or any text editor you like).

⚠️ Restart all your temrinal windows to take into account this change.

For Windows:

- `System Properties > Advanced> Environment Variables.`
- Locate the Variable name `PYTHONPATH`
- Add the path to `C:\path\to\olist`
