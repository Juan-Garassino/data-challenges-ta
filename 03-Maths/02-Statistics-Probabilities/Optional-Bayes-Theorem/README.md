## Bayes Theorem - a manual proof

In thise exercise, we have a dataset of 'Weather' conditions (Rain, Sunny, Overcast), and corresponding ‘Play’ conditions (Yes or No), suggesting possibilities of playing sports or not depending on weather conditions.

```python
weather_data= ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
play_data   =['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
```
Where the index i in `weather` correspond to the index i in `play`. For example, the 3th game, the weather was Overcast and they played game.

Our goal is to compute the probability $P(play|weather)$ to be able to anticipate if a new match will be allowed to take place tomorrow given a new weather condition.

In doing so, we will also demonstrate the followig **Bayes Theorem** by counting ourself each of these 4 probabilities:

$$P(play|weather) = \frac{P(play) P(weather|play)}{P(weather)}$$
$$Posterior = \frac{Prior * Likelihood}{constant}$$

Where :
- P(play) is our **prior** belief on the probability of the class (Play = Yes or No) given all data we have seen so far.
- P(weather|play) is the **likelihood** of seeing this type of weather (evidence), given that the match has played or not
- P(play|weather) is the **posterior** probability of actually playing or not, given the weather condition
- P(weather) is a constant that does not affect

Let's start!

### 0. Frequency Table
To see things clearly, start by constructing **manually** the frequency table (use a sheet of paper!). It should look like this :

| Weather  | Play  | Pause |
| ---------| ----- | ----- |
| Overcast |       |       |
| Sunny    |       |       |
| Rain     |       |       |
| Total    |       |       |


### 1. Calculate the prior probability $P(play)$
The idea is to compute the probability with a python logic, in case you have a much longer dataset!
Implement the function, `prior_probability(play, play_data)`. This should return the probability that the play happened.
for example :
```python
play = "Yes"
play_data = ["Yes", "No", "Yes"]
prior_probability(event, list_events)
==> 0.66666
```

### 2. Likelihood $P(weather|play)$

Well done, now we will implement a function to calculate the likelihood of observing a given weather, knowing that the match has been played or not. Basically, that means that we want to calculate the probability of an event (ex: weather = 'Sunny') being True given that the other event (ex: play=Yes) was True

Implement the function `likelihood(weather, play, weather_data, play_data)`. This function should return the probability that `event_condition` takes a given value, knowing `event_occur` value.

For example, given the following array, you should get this result :
```python
weather_data = ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
play_data   = ['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
likelihood("Sunny", "Yes", weather, play) = 3/9 = 0.33333
```

### 3. Posterior Probability $P(play|weather)$

Congratulations, it's almost finished.

❓ Using the Bayes Theorem and the two function coded before, implement the function `posterior_probability(play, weather, weather_data, play_data)` which gives you $P(play|weather)$

❓ Compare the result you found with a direct counting of P(play|weather) using the likelihood function with arguments reversed:
`likelihood(play, weather, play_data, weather_data)`

### 4. Step back and understand

Thanks to what you learned in this challenge could you answer these questions :
- Players will play if weather is sunny. Is this statement is correct?
- You know for sure, it will be raining for the next game. Do you think the game will be cancelled?



