## Team Project!

We have seen throughout the week that location, product categories or seller can impact review score.

Fundamentally review score can translate in lower business performance over the long term.

In this section, your goal is to produce an analysis that will inform which decision Olist CEO should take.

### Unit Economics

***Revenue***

As we have detailed previously, Olist charges sellers with various fees. For simplicity, we will assume that Olist takes 20% of the `booking_value` of sellers and charge 80 BRL by month per seller.

👉 Note: The `booking_value` is defined as the sum of product `price`. It excludes `freight_value`.

***Cost***

On the long term, bad customer experience has business implications: low repeat rate, immediate customer support cost, refund or non favorable word of mouth.

We will assume that we have an estimate measure of the monetary cost (in Brazilian Real) for each review:

review_score|cost (BRL)
---|---
1|100
2|50
3|40
4|0
5|0

In addition, we estimate that it costs 500 BRL to acquire one seller due to sales acquisition and marketing costs.

### The CEO's request

Your goal is to increase Olist customer satisfaction and margin while maintaining a healthy order volume.

You have been tasked by Olist CEO to study the impact and come with a recommendation for one or more of the suggestion below:
- Olist restrict deliveries to certain states.
- Olist implements a `review_score` threshold for sellers. Below that threshold, sellers get removed from the platform.
- Olist focuses its offering to some product categories.

### Your output

Your task is to produce, per team, a cost-benefit analysis of one or more recommendations as suggested above.

You are free to deep dive on one of the 3 option above, or evaluate each of them in less detail

### Present your analysis to the class at 4pm as a Team

- You have 10 minutes per group to convince Olist CEO of your recommendations

- Don't forget to explain the context, and the reasonning behing your recommendations

- Remember: Olist CEO is **not** a data scientist!

- Use Jupyter Noteobook **nbconvert** to make a slide-based presentation
```bash
jupyter nbconvert --to slides --post serve <your_notebook.ipynb>
```

