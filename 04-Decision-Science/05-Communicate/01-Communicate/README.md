## CEO Request

Our preliminary analysis is good enough for the limited time we have.

Let's recap our key findings:

We have seen how `wait_time` was the most significant factor explaining low review scores, but reading comments of the bad reviews also showed that some of them were linked to the seller or to the product itself.

Besides, `wait_time` is not known ahead of the order, and thus can hardly be acted-upon by your data-consulting team as an actionable recommendation to the Olist CEO directly.

On the contrary, you have built an analysis of sellers and products that demonstrated how some sellers, products, product categories and states can all negatively impact `review_score`, which translate into lower business performance over the long term.

ℹ️ We recommand you to focus on finishing the analyses of `products.ipynb` **or** `sellers.ipynb` before moving on.

What about potentially removing some of them from Olist marketplace, at least for those who persistently under-perform ? That may slighly reduce revenues but increase profit margin.

You have until Friday afternoon to produce a cost/benefit analysis for the recommendations of your choice, that will inform which decision Olist CEO should take in order to

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
- Olist restricts seller/customer matching between certain states?
- Repetitively underperforming sellers get removed from the platform after a while?
- Olist removes the worst performing products from its marketplace?
- Olist focuses on some product categories only?
- Olist acquire new sellers, with some assumption?
- Any combination of all of the above suggestions?
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
