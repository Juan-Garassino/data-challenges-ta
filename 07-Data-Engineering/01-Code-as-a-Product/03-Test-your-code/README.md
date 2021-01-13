
## Objective

Understand how tests work and implement your first test.

Install the code coverage package with `pip install coverage`.

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
