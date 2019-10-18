## Background

For this exercise, we will flip a coin (each flip has an equal chance of coming up heads or tails). This kind of experiment has no memory, in other words "flip is independent". Even though there is no way to predict what will be the next flip, if we flip a coin a number of times, the laws of probability allow us to predict the probability of obtaining various results. The accuracy will be greater as the number of flips increases.

## Four Flips

Quick reminder : a probability of 0 means a event will never occur. A probability of 1 means it will happen for sure.

Let's start smoothly : Suppose we flip a coin 4 times. Can you answer the following questions :
- How many possible outcomes could happen?
- What's the probability to get 4 heads?
- What's the probability to get 2 heads and 2 tails?

To answer these "easy" questions, you could count the number of ways to get a result. For example, there are 6 ways to get 2 heads and 2 counts :
- 1 1 0 0
- 1 0 1 0
- 1 0 0 1
- 0 1 1 0
- 0 1 0 1
- 0 0 1 1

And there are 16 possible outcomes. That means that the probability is P(4) = 6/16 = 0.375. But if the number of flips is larger, it becomes more difficult to count manually the different possibilities.

Mathematically, the number of ways to get x heads (or tails) in n flips could be calculated as :
```python
possibities = fact(n)/(fact(x)*fact(n-x))
```
where fact(n) means factorial of n :
fact(4) = 4 x 3 x 2 x 1 = 24

So for this exercise, implement the functions in `flip_coins_factorial.py` and try to pass the tests.

## Vizualize the data

Open jupyter notebook :
```python
jupyter notebook
```
Go into the Notebook we prepared for you and import the functions you just created. In an histogram, plot the output of probability(n_toss) with different values for n_heads and a fixed value for n_toss (each bar corresponds to a different n_heads). What can you notice?

If your implementation is correct, the more flips you do (n_toss increases), the more the graph becomes smoother and approaches the “bell curve”, or **normal distribution**. Try For example `n_toss = 100`

## And in reality?

You've already made big strides. But at this point, we could ask ourselves: *does the real world behave this way?*
Again, let's use the power of Python to answer this question.

For this exercise, implement the functions inside `simulate_reality.py`:

**play_one_game(n_toss):**
One game consists in flipping a coin n_toss times. This function should return the number of heads you get.
One way to do that is by randomly choosing an integer between 0 (head) and 1 (tail).
If you get 0, you increment your heads_counter otherwise it stays the same.
Your function should return the heads_counter (Hint: have a look at the [random library](https://docs.python.org/3/library/random.html))

**play_n_game(n_games, n_toss):**
Imagine you repeat the previous game `n_games` times.

The goal here is to play a bunch of flip coin games and see the distribution of the values we get from flipping a coin `n_toss` times.
This new function will call your previously defined `play_one_game` function `n_games` times. Then, we want to keep track of the end result of each game played this way.
`play_n_game` should return a dictionary. The keys will be the possible results of each game, so they can't be over `n_toss` or under 0. The values for each of those keys will correspond to the probability of a game ending with that result.

EX : Imagine you play 3 times (=n_games) to flip the coin 3 times (=n_toss) and you get
- 1st game : 0 head + 3 tails
- 2nd game : 2 heads + 1 tail
- 3rd game : 3 heads + 0 tail

that means that, you got : 
- 1 time 0 head
- 0 time 1 head
- 1 time 2 heads
- 1 time 3 heads

So your result should look like :
result = {0:1/n_games, 1:0/n_games, 2:1/n_games, 3:1/n_games}


## Compare results with Mean Squared Error (MSE)

Good job, if you have a look at the 2 graphs (theory vs reality), you should notice that they look the same. But as usual, we need a proof, we need a number to confirm this intuition.

Implement the function `error_reality_theory(n_games, n_toss)` in the comparison.py file. This function should simply return the squared error between theorical and "actual" results (get through simulation).



