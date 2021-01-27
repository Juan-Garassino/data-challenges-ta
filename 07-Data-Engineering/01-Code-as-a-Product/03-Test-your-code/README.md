
## Objective

Understand how tests work and implement your first test.

Install the [code coverage](https://en.wikipedia.org/wiki/Code_coverage) package with `pip install coverage`.

💡 __The `coverage` package will be used by the `make` command when we `make test` in order to assess the amount of code covered by the tests. How does that work ? The `coverage` command installed by the package will verify whenever we run the tests how much of the code of the package gets executed. This gives us an indication of the risk of our program being buggy (0%: not great, 100% coverage: highly tested)__

## Run tests

Inspect `mlproject/lib.py`  and `tests/lib_test.py`.

Inspect `Makefile`, and run:

```bash
make test
```

You just ran all the tests under `test/`

## Create your own test

You will now test the `haversine()` function:

- Create a `tools.py` file under `mlproject/` where you will implement the `haversine()` function taking 4 coordinates as input and returning the haversine distance
- Create a `tool_test.py` file under `tests/` testing your `haversine()` function

Run `make test` again and check that your test passes.
