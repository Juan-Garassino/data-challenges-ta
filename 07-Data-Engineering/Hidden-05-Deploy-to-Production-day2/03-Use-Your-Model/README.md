# Objective

Use and evaluate your model

## Get Predictions from gcp python api 

Now complete `predict.py` file to obtain online predictions from google:
- implement get_test_data() and preprocess() functions   
        => Beware to use the same preprocess function as the on you used for training
- implement `convert_to_json_instances()` function to pass json arguments to json api
- Here some help on the predict_json function:

```python
import googleapiclient.discovery

def predict_json(project, model, instances, version=None):
    """Send json data to a deployed model for prediction. """

    service = googleapiclient.discovery.build('ml', 'v1')
    name = 'projects/{}/models/{}'.format(project, model)

    if version is not None:
        name += '/versions/{}'.format(version)

    response = service.projects().predict(
        name=name,
        body={'instances': instances}
    ).execute()

    if 'error' in response:
        raise RuntimeError(response['error'])

    return response['predictions']
```

Once completed, run:
```bash
python predict.py
```

Make sure you correctly defined all your variables, pip installed and imported every needed library

## To go further

Create a jupyter notebook to visualise your predictions :  
 - Are local predictions same as online predictions ?
 - Visualise predictions as using `seaborn.pairplot`, how good is your model ?
