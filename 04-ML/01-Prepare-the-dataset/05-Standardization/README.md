# Standardization

Certain Machine Learning algorithms assume that all features have a somewhat normal distribution, centered around zero and with a similar variance. However, that is rarely the case in wild datasets. A feature that has a significantly larger variance can overpower others and prevent the model to learn from them.

Standaridization transforms each feature by removing its mean value (u) and dividing it by its standard deviation (s). As such, it is centered at zero.

$$𝑧=(𝑥−𝑢)𝑠$$

```bash
jupyter notebook 05-Standardization.ipynb
```
