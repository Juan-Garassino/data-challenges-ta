# Autoencoders
In this notebook, we look at a particular architecture used in deep learning: autoencoders. Autoencoders are neural network architectures trained to output the input they were given (may seem strange but it's useful!). The interest comes from the fact that there is a bottleneck in the network architecture i.e. a layer with a low number of neurons. If the autoencoder can reproduce its input only from this low-dimensional representation of the smallest layer, it means that it captured the data at hand. They have many applications.
![autoencoder.png](attachment:autoencoder.png)

They are usually trained with an mean square error on the output.

Here, we will train a neural network to work on 28x28 grey images from the MNIST dataset, available in keras.