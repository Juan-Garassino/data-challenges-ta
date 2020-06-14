# Context

Now that we have already built a simple model, we want to make it better! The ultimate goal is having a model that makes more accurate predictions on the test set, hence getting a RMSE as low as possible.

**So what can we do?**

There are many different things that make models better:
- build and try to use different or more features
- test with different estimators (linear, non linear, etc..)
- tune hyperparameters


The problem is that it is often hard to keep track of this different experimentations. There are many different parameters that we can tune and many different combinations.  

👉 **[MLFlow](https://www.mlflow.org/docs/latest/concepts.html) is a very useful tool to help us in machine learning models iteration.**

In this series of exercise, you will get hands on using the [MLFlow Tracking Api](https://www.mlflow.org/docs/latest/tracking.html) in order to experiment with different features, models and parameters.

Since that now we have a good workflow to make model improvements, it is very important to track all our different experiments. We want to be able to save all our differents training runs and compare their performance.

This is what MLFlow tracking is about.

## MlFlow Quickstart
Install MLFlow:
```
pip install mlflow
```
launch mlflow server in your current directory `mlflow ui`
```
mlflow ui
```
Check [here](http://127.0.0.1:5000/#/) your local mlflow tracking server
MLFlow defines experiments and runs, you have different runs inside one experiment
For instance for experiment *model_experiment*, you'll have :
 - 1 run for a linear model
 - 1 run for Randomforest model
For each run you will logs parameters and metrics

Open `ml_flow_test.py` and create your first experiment and first 2 runs inside this experiment:

```python
from  mlflow.tracking import MlflowClient
EXPERIMENT_NAME = "test_experiment"
client = MlflowClient()
experiment_id = client.create_experiment(EXPERIMENT_NAME)

for model in ["linear", "Randomforest"]:
    run = client.create_run(experiment_id)
    client.log_metric(run.info.run_id, "rmse", 4.5)
    client.log_param(run.info.run_id, "model", model)
```

## Hosted MLFlow server

For simplicity purpose, le wagon ran `mlflow ui` on its own server so that we all have the same [mlflow server](http://35.210.166.253:5000/#/experiments/0) to log our future experiments

We will now log same parameter on remote instance. For that we will slightly modify `ml_flow_test.py` to log info to the remote server:
```python
import mlflow
from  mlflow.tracking import MlflowClient
EXPERIMENT_NAME = "test_experiment"
# Indicate mlflow toi log to remote server
mlflow.set_tracking_uri("http://35.210.166.253:5000")
client = MlflowClient()
# Here experiment name already exists so we just get its existing id
experiment_id = client.get_experiment_by_name(EXPERIMENT_NAME).experiment_id

yourname=None

if not yourname:
    print("please define your name, il will be used as a parameter to log")

for model in ["linear", "Randomforest"]:
    run = client.create_run(experiment_id)
    client.log_metric(run.info.run_id, "rmse", 4.5)
    client.log_param(run.info.run_id, "model", model)
    client.log_param(run.info.run_id, "student_name", yourname)
```
Check out  [mlflow server](http://35.210.166.253:5000) to visualise your logs

## Mlfow integrated to our Taxifare ml project
Now we will add a few methods to our existing class in order to start logging training runs
For that we will add following methods to our Trainer() class:
```python
class Trainer():
    ...

    ### all methods from last exercice above
    @memoized_property
    def mlflow_client(self):
        mlflow.set_tracking_uri(MLFLOW_URI)
        return MlflowClient()

    @memoized_property
    def mlflow_experiment_id(self):
        try:
            return self.mlflow_client.create_experiment(self.experiment_name)
        except BaseException:
            return self.mlflow_client.get_experiment_by_name(self.experiment_name).experiment_id

    @memoized_property
    def mlflow_run(self):
        return self.mlflow_client.create_run(self.mlflow_experiment_id)

    def mlflow_log_param(self, key, value):
        self.mlflow_client.log_param(self.mlflow_run.info.run_id, key, value)

    def mlflow_log_metric(self, key, value):
        self.mlflow_client.log_metric(self.mlflow_run.info.run_id, key, value)
```
Notice how [@memoized_property](https://pypi.org/project/memoized-property/) is actually quite powerfull:
- it is a decorator
- is defines its following function as a [property](https://www.geeksforgeeks.org/python-property-function/)
- the property is memoized <=> only set at first call

## Log first params and metrics
We've done the hard work, we can now easily log any param and metric by simply adding `self.mlflow_log_param(param, value)` or `self.mlflow_log_metric(metric_name, metric_value)` anywhere in our class:
- Define 2 global variables at the beginning `trainer.py`:
```python
MLFLOW_URI = "http://35.210.166.253:5000"
myname="youshouldwriteyournameinstead"
EXPERIMENT_NAME = f"TaxifareModel_{myname}"
```
- log the model name and rmse at correct place inside `Trainer()` class
- run whole workflow:
```
python -m TaxiFareModel.trainer
```
- check it logged correctly  on [wagon hosted mlflow server](http://35.210.166.253:5000/)
