## CEO Request

Our preliminary analysis is good enough for the limited time we have.

Let's recap our key findings:

We have seen how `wait_time` was the most significant factor explaining low review scores, but reading comments of the bad reviews also showed that some of them were linked to the seller or to the product itself.

Besides, `wait_time` is not known ahead of the order, and thus can hardly be acted-upon by your data-consulting team as an actionable recommendation to the Olist CEO directly.

On the contrary, you have built an analysis of sellers (and opt. products) that demonstrated how some sellers, products, or product categories can all negatively impact `review_score`, which translate into lower business performance over the long term.

What about potentially banning some sellers/products from Olist marketplace, at least for those who persistently under-perform ? That may slighly reduce revenues but increase profit margin, as described below

### Unit Economics

***Revenue***

As we have detailed previously, Olist charges sellers with various fees. For simplicity, we will assume that Olist takes a **10% cut** on the product price of each order delivered and charge **80 BRL by month** per seller.

👉 Note: The product `price` excludes any `freight_value`

***Cost***

- On the long term, bad customer experience has business implications: low repeat rate, immediate customer support cost, refund or non favorable word of mouth.

We will assume that we have an estimate measure of the monetary cost for each bad review:

review_score|cost (BRL)
---|---
1|100
2|50
3|40
4|0
5|0

- In addition, Olist experiences internal **IT costs**, which can be considered approximatively proportional to the square-root of the number of orders processed (think scaling effects). Since inception, total IT costs amounted to 500,000 BRL.

- Finally, we estimate that it costs 800 BRL to acquire one new seller due to sales acquisition and marketing costs.

### Your turn!

Time to start from a blank Notebook and re-use what we have already coded in our `olist` package.
(don't try to re-use previous notebooks, which were made for investigation only!)

Open the `ceo_request.ipynb` notebook and start from there.

You have until Friday afternoon to produce a cost/benefit analysis for the recommendations of your choice, that will inform which decision Olist CEO should take in order to

> _increase Olist customer satisfaction and margin while maintaining a healthy order volume_

Your task is to produce a detailed cost-benefit analysis of one or more recommendations as discussed above.
- Olist removes underperforming sellers from the platform?
- Olist removes only repetively underperforming sellers, after a honeymoon period of few months
- Olist restricts (seller,customer) combination between certain states to avoid delays?
- Olist removes the worst performing products / categories from its marketplace entirely?
- Olist acquire new sellers, with some assumption to be suggested?
- Any combination of all of the above suggestions?
- ...


### Tomorrow evening, you will present your analysis in front of your favorite TAs & classmates!

You have 10 minutes max per person (discussion included) to convince Olist CEO of your recommendations.

- A TA will play the role of the CEO
- You will be paired by group of 4/6 students for each TA

Don't forget to explain the context, and the reasonning behing your recommendations

Remember: Olist CEO is not a data scientist!

👉 You will have to make a slide-based presentation using Jupyter Noteobook **nbconvert**

```bash
jupyter nbconvert --to slides --post serve <your_notebook.ipynb>
```
