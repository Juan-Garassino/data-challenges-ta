## Objective

Create first sklearn pipeline  
No GCP here, everything on your laptop 

## First simple pipeline

- Open `trainer/train.py `file  
- Complete class `Preprocessing()` with preprocessing function from yesterday's challenge
- Read function `perf_eval_regression() `from `trainer/tools.py` and test your first pipeline


    python -m trainer.train

## Pipeline with dependencies

Now let us structure our code for clarity purpose  

We'll move every Pipeline bloc in a separate python file:
- Create a new a file `trainer/pipeline_blocs.py`, and move `Processing()` from `train.py` to `pipeline_blocs.py`  
- Import it into `trainer/train.py` and run it again to check import

