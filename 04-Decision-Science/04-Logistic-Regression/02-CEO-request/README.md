## ⚠️ Finish yesterday's challange 02 first
**Take your time to finish and understand entirely `sellers.ipynb` analysis and code the associated `seller.py` before moving to this final challenge**


## CEO Request

Our preliminary analysis is good enough for the limited time we have. Let's recap our key findings:
- We have seen how `wait_time` was the most significant factor explaining low review scores, but reading comments of the bad reviews also showed that some of them were linked to the seller or to the product itself.
- `wait_time` is made of seller's `delay_to_carrier` + `carrier_delivery_time`. The latter being outside of Olist's direct control, improving it is not a quick-win recommendation we can make to Olist CEO without in-depth analysis of their operational practices.
- On the contrary, better selecting `sellers` can positive impact on `delay_to_carrier` and reduce the number of bad `review_score` on Olist.

💡 Let's investigate the economic impact of banning some sellers from Olist marketplace:

### Unit Economics

***Revenue***

- Olist takes a **10% cut** on the product price (excl. freight) of each order delivered.
- Olist charges **80 BRL by month** per seller.

***Cost***

- On the long term, bad customer experience has business implications: low repeat rate, immediate customer support cost, refund or non favorable word of mouth. We will assume that we have an estimate measure of the monetary cost for each bad review:
review_score|cost (BRL)
---|---
1|100
2|50
3|40
4|0
5|0
- In addition, Olist's digital infrastructure incurs **IT costs** which can be considered approximatively **proportional to the square-root of the number of orders processed** (think scaling effects). Since inception of the marketplace, cumulated IT cost have amounted to 500,000 BRL.

### ✏️ Your turn!

👉 **Open the `ceo_request.ipynb` notebook and start from there.**

- We'll start from a blank Notebook and re-use what we have already coded in our `olist` package
- We don't recommend to re-open previous notebooks, which were made for investigation only!
- You have until Friday afternoon to produce the following cost/benefit analysis: Should Olist removes underperforming sellers from the platform? What would have happened if it had done so ? (what-if analysis)

### (Optional)
If you are done with the first recommendation, feel free to finetune your investigation as per below:
- Add temporality to your analysis: What if Olist had only removed repetively underperforming sellers, after a honeymoon period of few months ?
- Investigate a restriction on distance_seller_customer or (seller_state, customer_state) tuple?
- What about removing the worse performing performing products from its marketplace entirely?
- Any combination of all of the above suggestions?
- ...

### (Tomorrow evening) you will present your analysis to your favorite TAs & classmates!

You have 10 minutes max per person (discussion included) to convince Olist CEO of your recommendations.

- A TA will play the role of the CEO
- You will be paired by group of 4/6 students for each TA

Don't forget to explain the context, and the reasonning behing your recommendations

Remember: Olist CEO is not a data scientist!
