## Boosting

Adaboost is a very good method and easy to use quickly. It's differentt from Bagging and Random Forest.

In bagging and RF : we wanted **low bias, high variance model**. In Boosting, we want **high bias models** ("weak learners"). Weak learners mean that they will have classification accuracy close to 50-60% (not better than chance).

The main idea behinh boosting is that by combining many weak learners we can get a strong learner.

## Weak Learners

To get/create weak learners, we choose decision tree with max_depth equal to 1. That means that we only split the space in a hald for each tree. You should admit that's quiet fascinating that a combination of that could yield to a strong learner no?

Another way to "create" weak learner is to use a simple linear classifier (like logistic regression).

A first advantage of this method is that weak learner train fast 🤓, so we can easily train a lot of these learners !

## The AdaBoost algorithm

With Adaboost we will use -1 and 1 for the target (and not 0 and 1). It will be clearer why when we see the algorithm.

The main steps of the algorith are :
- Add  one base model at a time
- Train base model on all data (not as bootstrapping/resampling)
- Instead we will weight how important each sample is with w_i (i=1..N)
- Modify w_i on each round
- If we get (x_i, y_i) wront then increase w_i, else, decrease w_i

In pseudo-code :
```
w[i] = 1/N for i=1..N
for m=1..M:
  fit f_m(x) with sample weights w[i]
  epsilon_m = sum(w[i]*I)/sum(w[i]) --> error rate
  alpha_m = 1/2 * log ((1-epsilon_m)/epsilon_m) --> log "correct" rate
  w[i] = w[i] * exp(alpha_m * y[i] * f_m) for i=1..N
  w[i] = w[i]/sum(w[i])
  save alpha_m, f_m
```

## Exponential Loss Function

With Adaboost, we will use the exponential loss function :
```
L(y, f(x)) = exp(-y*f(x))
```
--> if y and f(x) same signs --> 0
--> if y and f(x) opposite signs --> infinity

The goal of this challenge is to get the main idea. we will use the method from Scikit-Learn but it's always good to know what's behing the scene.
