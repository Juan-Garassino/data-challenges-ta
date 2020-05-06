## Multivariate Regression 🌞

We are finally ready to start investigating explaining factors for customer satisfaction using our newly coded training data!

```python
from olist.order import Order
data = Order().get_training_data()
```

We will use a multivariate linear regression with [statsmodels](statsmodels.org) to measure order features importance on customer satisfaction. Make sure to install it using:

```bash
pip install statsmodels==0.10.1
```

Open `notebooks/02_02_mutivariate_regression.ipynb` and follows instructions
