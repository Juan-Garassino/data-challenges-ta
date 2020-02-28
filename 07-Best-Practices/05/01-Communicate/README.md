## Team Project!

We have seen throughout the week that location, product categories or seller can impact review score.

Fundamentally review score can translate in lower business performance over the long term.

In this section, your goal is to produce an analysis that will inform which decision Olist CEO should take.

### Unit Economics

***Revenue***

As we have detailed previously, Olist charges sellers with various fees. For simplicity, we will assume that Olist takes a **10% cut** on the product price of each order delivered and charge **80 BRL by month** per seller.

👉 Note: The product `price` excludes any `freight_value`

***Cost***

On the long term, bad customer experience has business implications: low repeat rate, immediate customer support cost, refund or non favorable word of mouth.

We will assume that we have an estimate measure of the monetary cost for each bad review:

review_score|cost (BRL)
---|---
1|500
2|300
3|100
4|0
5|0

In addition, we estimate that it costs 800 BRL to acquire one seller due to sales acquisition and marketing costs.

### The CEO's request

You have been tasked by Olist CEO come with recommendations on **how to increase Olist customer satisfaction and margin while maintaining a healthy order volume**

Hint: Below is a list of possible suggestion to explore (among other)
- Olist restrict seller/customer matching between certain states
- Olist implements a review_score threshold for sellers. Repetitively underperforming sellers get removed from the platform after a while.
- Olist focuses its offering to some product categories, or remove some specific products from its platform
- ...

### Your output

Your task is to produce, per team, a cost-benefit analysis of one or more recommendations as suggested above.

### Present your analysis to the class at 4pm as a team

You have 10 minutes max per group (discussion included) to convince Olist CEO of your recommendations

Don't forget to explain the context, and the reasonning behing your recommendations

Remember: Olist CEO is not a data scientist!

Use Jupyter Noteobook **nbconvert** to make a slide-based presentation

```bash
jupyter nbconvert --to slides --post serve <your_notebook.ipynb>
```
