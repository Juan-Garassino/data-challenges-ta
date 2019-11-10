In this notebook, you will create 2D data that corresponds to two _moons_: each moon corresponds to a given number of samples, each being a 2D input. Each moon, i.e. all the points of the moon, corresponds to a label, `0` or `1`. These moons are more or less noisy, depending on a `noise` parameters, and the corresponding labels cannot be linearly separated.

Here is an example of such moons:

![moons](./moons_example.png)

To separate the moons, you will build your first Neural Network that takes as input the 2D values of each point and outputs a label, `0` or `1`. In this notebook, we will go progressively through different aspects of the neural network architecture and training procedure.

To start the exercise open `01-classification.ipynb`.
