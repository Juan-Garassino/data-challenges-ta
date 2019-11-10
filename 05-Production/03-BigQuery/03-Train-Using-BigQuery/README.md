# Train the taxi fare prediction model with the entire dataset.

It is time to train the model using 50+ millions rows. 
For this, you will connect directly to BigQuery and train a model with all the data.

## Install python package to query BigQuery

To load data from BiQuery you will need to use the python API.
For that, install `google-cloud-bigquery` with:

```bash
pip install google-cloud-bigquery
``` 

## Train with all data!

- Go back from yesterday's code, you'll be given less information than yesterday
- Modify task.py to connect to BiqQuery and load data  
    ==> Test it on a small sample first

Now let's train it on 20 million lines (50 will take too long)
- Create a Makefile to train online, and deploy model with a new version  
    => Don't forget all necessary files for dependencies, custom Predictor, etc ...
    
**_Loading 55 million lines might require higher RAM/CPU capacity_**  
==> think twice before choosing the [instance](https://cloud.google.com/ml-engine/docs/training-at-scale) you want 

- Make predictions with your trained model on a sample of the test set
- Compare your the accuracy of your new model to you previous ones
