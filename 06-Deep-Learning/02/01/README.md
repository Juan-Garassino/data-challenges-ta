## Plan and objectives:

In this notebook, we propose to define a simple baseline cnn, train it and evaluate it on cifar-10 dataset. This dataset consists of 32x32 images of 10 different categories. 

 We will then introduce data augmentation: a method designed to arbitrarily augment the training data set by computing perturbations of the train images (random crops, intensity changes etc) and show how it allows to improve the generalization.

For now, we stick to computations on CPU, but bear in mind that a model training takes ~10 minutes on CPU in this notebook, so don't waste your trainings !

When you reach the end of the data augmentation, please go to exercise 2 and 3 before coming back to dropout and batch normalization.
