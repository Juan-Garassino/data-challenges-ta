# Objective

Let's improve our model by tuning its hyperparameters.
For this we can leverage Google Cloud computation power to search for the best parameters.

## HyperParameter tuning
Get code From last exercice 

- Open up `trainer.py`
- Implement a grid search using [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) to find the best parameters for your estimator.
- Respect naming of parameters dict to feed to GridSearchCV, check [medium article](https://medium.com/@yoni.levine/how-to-grid-search-with-a-pipeline-93147835d916)
- With a GBM model, you can search for the best learning_rate for example, while choosing a fixed value for number of trees.

## Deploy to GCP and evaluate performance

Try change the machine types to speedup the training when doing expensive grid search.  
Check [GCP VM pricing](https://cloud.google.com/compute/all-pricing), then add these parameters to your `gcp_submit_training` make command:

```bash
gcp_submit_training:
    @gcloud ai-platform jobs submit training ${JOB_NAME} \
    ... \ 
    --scale-tier CUSTOM \
    --master-machine-type n1-standard-16
```
Check [documentation](https://cloud.google.com/ml-engine/docs/machine-types) if needed

How much did your model improve vs without grid search ?

NB : you might need to deploy a new version here to compare results

## To go further
Read this interesting [medium article](https://towardsdatascience.com/hyperparameter-tuning-on-google-cloud-platform-with-scikit-learn-7d6155195efb) explaining how let GCP do the hyperparameter tuning for you  

It is out of scope pour our project, but you can try and implement it yourself.

