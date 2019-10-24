## Objective

Use and evaluate your model 

## First locally

First complete `predict.py` file to evaluate the model locally

## Then using AI Platform 

The command we'll use here is `gcloud ai-platform predict`  

Check documentation for online prediction

    gcloud ai-platform predict --help
    
Create an input.json file with each input instance on a separate line, i.e :

    [6.8,  2.8,  4.8,  1.4]
    [6.0,  3.4,  4.5,  1.6]
    
Use command to obtain predictions  
save predictions to csv  
evaluate your model  
