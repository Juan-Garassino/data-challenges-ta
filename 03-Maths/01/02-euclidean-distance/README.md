# Foreword

A very important notion for data scientists is the concept of **distance**. During the next weeks, we will use it almost every day.

For example, when you train a model in order to make predictions, you need to evaluate the precision of your model. A good approach to measure that, is to compute the distance between the actual result and your predictions.

## Do you remember Pythagore?

The Pythagorean theorem says that the area of a square on the hypotenuse is equal to the sum of the areas of the squares on the legs. In this picture, the area of the blue square added to the area of the red square makes the area of the purple square. It was named after the Greek mathematician Pythagoras:

If the lengths of the legs are a and b, and the length of the hypotenuse is c, then, `a^2+b^2=c^2`

![Pythagore representation](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Pythagorean_right_angle.svg/220px-Pythagorean_right_angle.svg.png)

In this exercise, you will have to implement the function `hypotenuse(a, b)` in pythagore.py. This function should return the length of the hypotenuse or 0 if any problems.

## Euclidean distance in 2D

Well done ! Now you will compute the euclidean distance between points in 2 dimensions. To complete this challenge, you have to implement the functions inside the `euclidean_distance_2d.py` file:
- `euclidean_distance_p2p(p_1, p_2)`: return the distance between p_1 and p_2;
- `calcul_hypotenuse_with_points(p_1, p_2, p_3)`: return the hypotenuse of the triangle using the Pythagorean theorem (first, you should calculate the length of the 2 segments and then apply Pythagore);
- `euclidean_distance_p2dr(p_1, pente, origin)`: return the shortest distance between a point and a line segment (more information [here](https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line));
- `error_predictions(actual_results, predictions)`: return an array containing the distance (=the "error") between all results in actual_result and all predictions;
- `points_in_circle(points, center, rad)`: return an array of points containing all the points that fit into a circle (center=(x,y)) with radius rad. We add a visual check for this one!

As a quick reminder, if you have 2 points `p1(x1, y1)` and `p2(x2, y2)`, then the distance between p1 and p2 will be `d = sqrt((x1^2 - x2^2) + (y1^2 - y2^2)^2)`.

<img src="https://res.cloudinary.com/wagon/image/upload/v1571239306/Screenshot_2019-10-16_at_17.21.14_wt3jpz.png" height="50%" width="50%">

Note that sometimes this distance is called "the norm of the vector". In 2 dimensions, that means the length of the vector.

## Euclidean distance in 3D

Until now, we have compute the distance between points in 2 dimensions (x and y). It's a good approach to get some intuition about the notion of distance. However, most of the time, during your Data Scientist life, you will not work in 2-D but in n-D (and n can be very large !).

Imagine you want to construct a model based one 10.000 features (for example, image (100px x 100px) recognition). Then you will compute the cost function, predictions, errors,... in 10.000-dimension. It will be much more complicated to visualize. However, the concept stays "as simple as before".

Let's start with an easy one!
We say "easy" because it's still easy to visualize : we will compute the distance between 2 points in 3D.

For this challenge, you will implement the function inside `euclidean_distance_3d.py`

## 4. Distance in n dimensions

Well done ! Now we will define the "distance" based on much more dimensions. For example, we could define the distance between 2 flats based on the following features ("dimensions")
- feature_1 : number of rooms
- feature_2 : number of bathrooms
- feature_3 : Surface of the house[m^2]
- ...
- feature_n : Surface of the garden[m^2]

- calcul la distance entre 2 appartements basés sur 10 critères
- calcul la distance entre 1000 appartements basés sur 10 critères

