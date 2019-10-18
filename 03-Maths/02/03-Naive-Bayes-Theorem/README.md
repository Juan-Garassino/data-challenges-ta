It is a **classification technique** based on Bayes’ Theorem with an assumption of independence among predictors. In simple terms, a Naive Bayes classifier assumes that the presence of a particular feature in a class is unrelated to the presence of any other feature.

In thise exercise, we have a dataset of weather and corresponding target variable ‘Play’ (suggesting possibilities of playing sports). Now, we need to classify whether players will play or not based on weather condition. Let’s follow the below steps to perform it.

![Formule de Bayes](https://www.bayestheorem.net/images/Bayes-Theorem-Formula-Defined.jpeg)

Where :
- P(A|B) is the probability of A if B (posterior probability)
- P(A) is the probability of A (priori probability)
- P(B|A) is the probability of B if A
- P(B) is the probability of B


## Calculate the prior probability
Imagine we have the following data about previous games :
```python
weather= ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
play   =['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
```
Where the index i in `weather` correspond to the index i in `play`. For example, the 3th game, the weather was Overcast and they played game.

To start this exercise, construct the frequency table. To help you, you could do it manually on a sheet of paper. It should look like this :
```python
 ___________________________
| Weather  |   No   |  Yes  |
|__________|________|_______|
| Overcast |        |       |
|__________|________|_______|
| Sunny    |        |       |
|__________|________|_______|
| Rain     |        |       |
|__________|________|_______|
| Total    |        |       |
|__________|________|_______|
```
Now to help you to do that (if you had more data, you could not do it mannualy), implement the function, `prior_probability(event, list_events)`. This should return the probability that the `event` happens.
for example :
```python
event = "Sunny"
list_events = ["Sunny", "Rainy", "Sunny"]
prior_probability(event, list_events)
==> 0.66666
```

## Posterior Probability

Well done, now we will implement a function to calculate the posterior probability. Basically, that means that we want to calculate the probability of an event "A" being True knowing that another event "B" is True. Again, you could start by completing manually the likelihood table.

Implement the function `posterior_probability(event_occur, event_condition, weather, play)`. This function should return the probability that the event `event_occur` happens knowing that `event_condition` is True.

For example, given the following array, you should get this result :
```python
weather= ['Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy','Rainy','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
play   =['No','Yes','Yes','Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','Yes','No']
posterior_probability("Sunny", "Yes", weather, play) = 3/9 = 0.33333
```

## Bayes Probability

Congratulations, it's almost finished. You just have to implement the function `bayes_probability(event_occur, event_condition, list_occur, list_condition)`. As explained at the beginning of this article, this can be calculated like this :

P(A|B) = P(B|A) * P(A)/P(B)

As you can notice, we have all the tools we need to compute this function. Let's do this !

Thanks to what you learned in this challenge could you answer these questions :
- Players will play if weather is sunny. Is this statement is correct?
- You know for sure, it will be raining for the next game. Do you think the game will be cancelled?

with the following data :
```python
play  = ['No', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No']
weather = ['Rainy', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Rainy', 'Sunny', 'Overcast', 'Sunny', 'Rainy', 'Sunny', 'Rainy', 'Rainy', 'Sunny', 'Rainy', 'Overcast', 'Overcast', 'Rainy', 'Rainy', 'Overcast']
```
