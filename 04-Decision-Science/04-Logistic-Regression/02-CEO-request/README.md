## CEO Request

Our preliminary analysis is over. We have seen how location, product categories, sellers can all negatively impact `review_score`, which translates into lower business performance over the long term.

You have until Friday afternoon to produce a cost/benefit analysis that will inform which decision Olist CEO should take, in order to

> _increase Olist customer satisfaction and margin while maintaining a healthy order volume_


### Unit Economics

***Revenue***

As we have detailed previously, Olist charges sellers with various fees. For simplicity, we will assume that Olist takes a **10% cut** on the product price of each order delivered and charge **80 BRL by month** per seller.

👉 Note: The product `price` excludes any `freight_value`

***Cost***

On the long term, bad customer experience has business implications: low repeat rate, immediate customer support cost, refund or non favorable word of mouth.

We will assume that we have an estimate measure of the monetary cost for each bad review:

review_score|cost (BRL)
---|---
1|100
2|50
3|40
4|0
5|0

In addition, we estimate that it costs 800 BRL to acquire one seller due to sales acquisition and marketing costs.

### Your objective

Your task is to produce a detailed cost-benefit analysis of one or more recommendations as suggested above.

Hint: Below is a list of possible suggestion to explore (among other)
- Olist restrict seller/customer matching between certain states
- Olist implements a review_score threshold for sellers. Repetitively underperforming sellers get removed from the platform after a while.
- Olist focuses its offering to some product categories, or remove some specific products from its platform
- Olist acquire new sellers
- ...


### Present your analysis to your whereby room, Friday afternoon at 5pm

You have 15 minutes max per person (discussion included) to convince Olist CEO of your recommendations.

- A teacher assistant will play the role of the CEO
- Other whereby room members will also attend allowed to ask questions

Don't forget to explain the context, and the reasonning behing your recommendations

Remember: Olist CEO is not a data scientist!

👉 You will have to make a slide-based presentation using Jupyter Noteobook **nbconvert**

```bash
jupyter nbconvert --to slides --post serve <your_notebook.ipynb>
```
