# This last exercise is a real challenge.

You are given real data, for which the goal is to set the neural network that has the best architecture to predict the problem at hand. This means that you should optimize :

- The architecture of the Neural network (NN) : number of layers, number of neurons, activation functions, ...
- The loss of the NN
- The optimizer of the NN

This should be all done in a Cross-validation setting to make sure that you do not overfit one split of the testing data!



The data you are given are from the abalone dataset (http://archive.ics.uci.edu/ml/datasets/Abalone)

The abalone is a shell from which you are given multiple properties and you have to infer its age.
1. Download the data directly from the website
2. Split it into X and y
3. Do one train/test split
4. Find one suitable architecture, loss, optimizer, ...
5. Once you have a full pipeline, evaluate it in a cross-validation procedure
