Let's start with a very simple exercise to understand how these exercises are going to work.

## Check

Some of the exercises will have a `check.sh` bash script. This script will check if your challenge is correct (using [Test-Driven Development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development) where tests have been written beforehand by Le Wagon's teachers). To run this script in your terminal, `cd` to the proper folder (as explained above ☝️) and run:

```bash
./check.sh
```

## How to solve a challenge

Your goal is to implement the method `sum3` in the `sum_of_three.py` file. Before you actually try to do it, run the **tests** that we prepared:

```bash
pytest
```

You should get three failing tests. Read the error (especially the `AssertionError`) to understand what is wrong and try implementing the `sum3` method in the `sum_of_three.py` file. When you are done, run the command above once again.

Repeat until all tests turn pass (i.e. `0 FAILED`)

Then check your style with:

```bash
pylint sum_of_three.py
```

If you get style errors, fix them, save and re-run the command above.

## Conclusion

The goal of this exercise was to show you how to run the tests to automatically evaluate your code (both style & content) and introduce you to this tight feedback loop.
