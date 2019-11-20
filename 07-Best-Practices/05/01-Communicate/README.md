## Communicate 

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

### Projects 

You have been tasked by Olist CEO to study the impact and come with a recommendation for **one of** the project below. 

Your goal is to increase Olist customer satisfaction and margin while maintaining a healthy order volume. 

Pick one of the project below: 

- Olist restrict deliveries to certain states. 
- Olist implements a `review_score` threshold for sellers. Below that threshold, sellers get removed from the platform. 
- Olist focuses its offering to some product categories.

### Output 

For **one** of the project below, your task is to produce: 

- A notebook with your code and logic. 
- A one-pager document with your recommendations and main takeaways of your analysis. 

### Github & Peer-review 

[Peer view](https://en.wikipedia.org/wiki/Peer_review) is an important part of the scientific process. 

In order to make sure your analysis is rock solid, you will push your work on a Github repo and request a review to your buddy of the day via a Pull Request. 