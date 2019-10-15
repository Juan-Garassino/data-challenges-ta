# Interactive plot with Plotly
### Introduction

Same principle in this exercise, we are going to **recreate** plots from this [article](https://www.data-to-viz.com/story/ThreeNum.html).

To learn more **best practices** around bubble plot read these **3 short articles**.

[Radius or Area](https://www.data-to-viz.com/caveat/radius_or_area.html),
[Area lisibility](https://www.data-to-viz.com/caveat/area_hard.html),
[Overplotting](https://www.data-to-viz.com/caveat/overplotting.html)

### Dataset

You will work with the **GDP per capita** dataset.

[Download Link - https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/4_ThreeNum.csv](https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/4_ThreeNum.csv)

### First steps

Create a notebook named `exercise04.ipynb` in the **same folder** as this **README**.
Now you can **import** the necessesary **libraries**.

```python
import numpy as np
import pandas as pd
import matplotlib
%matplotlib inline
import seaborn as sns
```

Then **import** the **dataset** from the CSV you just downloaded.

### Part 1

Recreate this bubble plot with the **bubble size** in the **legend**.

Set the `hue` of your plot on the **continent**.

<img src="https://www.data-to-viz.com/story/ThreeNum_files/figure-html/unnamed-chunk-2-1.png" width="760">

### Part 2

Now add country name as **labels** for the countries where:
- the gdp per capita is greater than **5000**.
- the life expectancy is smaller than **65** years old.

<img src="https://www.data-to-viz.com/story/ThreeNum_files/figure-html/unnamed-chunk-4-1.png" width="760">

### Part 3

We will now use [Plotly](https://plot.ly/python/bubble-charts/) to create an **interactive** plot.
That way we will be able to:
- zoom in the chart
- lookup values for each data point

**Plotly install:**

```sh
conda install -c plotly plotly=4.1.0
```

<img src="https://i.ibb.co/9y0JLbF/Screen-Shot-2019-10-15-at-16-34-09.png" width="760">
