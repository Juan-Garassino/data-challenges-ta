## It's time to divide and conquer!

So far, we have seen the impact of some variables to the overall customer experience. Negative correlation with `wait_time` and `delay_vs_expected` was the most concluant finding, but we need to dig deeper.

The next two exercices will analyze which *product categories* and *seller* drive best customer satisfaction. Our goal is to identify patterns we will be able to use to increase quality supply.

We will answer questions like:

- What's the impact of product category or seller on customer rating?
- Other things being equal, what's the impact of the location to wait_time?
- Can we identify which sellers contribute the most to the longer wait time by delivering too late to the carrier?

### ⚡️⚡️Split your team in two for the day ⚡️⚡️
- One works on this exerice 2 (Products) while the other works on exercice 3 (Sellers)
- Then, share your results within your team, peer review your code and commit everything to your team repo.

## Exercice 2: Product Categories

We look at the impact of product categories on customer satisfaction and wait time.

### Preparation

- Create the method `get_training_data` method in `olist/product.py` that will return the following DataFrame:

  - `product_id` (_str_) _the id of the product_
  - `category` (_str_) _the category name (in english)_
  - `height` (_float_) _height of the product (in cm)_
  - `width` (_float_) _width of the product (in cm)_
  - `length` (_float_) _length of the product (in cm)_
  - `weight` (_float_) _weight of the product (in g)_
  - `price` (_float_) _average price sold of the product_
  - `freight_value` (_float_) _average value of freight_
  - `product_name_length` (_float_) _character length of product name_
  - `product_description_length` (_float_) _character length of product description_
  - `n_orders` (_int_) _the number of orders in which the product appeared_
  - `quantity` (_int_) _the total number of product sold_
  - `wait_time` (_float_) _the average wait time in days for orders in which the product was sold._
  - `share_of_five_stars` (_float_) _The share of five stars orders for orders in which the product was sold_
  - `share_of_one_stars` (_float_) _The share of one stars orders for orders in which the product was sold_
  - `review_score` (_float_) _Average review score_

### Analyse

Open `notebooks/03_02_product_impact.ipynb`and follows instructions (copied below)


#### Visualization

Let's start by looking at the performance of product categories:

- Create a DataFrame aggregating, for each product category, the following variables:

  - `n_orders` (sum)
  - `wait_time` (median)
  - `review_score` (median)
  - `share_of_one_stars` (median)
  - `share_of_five_stars` (median)

 - Plot a text scatterplot of each category by `n_orders` and `wait_time`.

👉 Hint: You can use the function `text_scatterplot` defined in `olist/utils.py`

- Hard to read, right? What about restricting to only categories that had 300 orders at least?

- Let's now look at the correlation between variables. Return a DataFrame with correlations coefficients between each variables within the category DataFrame. What do you remark?

- Plot few distribution plots on product characteristics (weight, height etc.) for high and low average wait time categories.

#### Wait Time

In this part, we will use a multivariate regression to isolate which product categories correlate with wait time.

- Run an OLS model and print out variables with significant coefficients. Which product categories correlate with higher wait_time?

👉 Hint: you can use the function `return_significative_coef` defined in `olist/utils.py`

#### Review score

We have seen before that some products correlate with higher wait time. One hypothesis being that some products being bigger or heavier, customer delivery take more time.

What about their correlation with review score?

- Create your target variable as the `average_review_score` and run an OLS model on `product_categories`. Which product categories correlate with higher `review_score`? Which tend to have lower `review_score`?

#### Review score, controlling for Wait Time

But can we isolate the true contribution of product category on customer satisfaction?

In this section, we will use `wait_time` as a dependent variable and measure how each product category correlate with `review_score`, holding `wait_time` constant.

- Run an OLS model `model_review_fixing_wait_time` where `product_categories` and `wait_time` are the regressors, and `review_score` is the target variable. Which product categories correlate with higher `review_score` holding `wait_time` constant?

#### (Optional) Reviews for low review score Products

- Using our translation script, translate a sample of reviews for some of the low review categories. Do you see topics that stand out?
