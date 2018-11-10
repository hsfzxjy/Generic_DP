# Generic_DP

This libary provides universal algorithms for dynamic programming problems.

## descriptive_dp

Module `descriptive_dp` provides a decorator `dp`, with which user can easily turn a recursion equation into efficient and descriptive code. `dp` decorated function will cache calculated results, and return them directly if same parameters passed again. No repetitive computation happens. And, if you wish, it may also record state transfering process, so you can have a better understanding of how the decisons are made.

`dp` accepts one boolean parameter `store_decisons`, which indicates whether to store state transfering process or not.

```python
@dp(store_decisions=True)
def f(stage, state):
    ...
```

The function to decorate should always accept two parameters `stage` and `state`, and returns a real number, representing the optimal value at this stage with state `state`.

When `store_decisons` set `True`, decorated function will have three new functions `select_min`, `select_max` and `get_decisions_path`, which are used for storing and obtaining decisions path.

```python
f.select_min(
    (current_stage, current_state),
    [
        ((next_stage_1, next_state_1), value_1),
        ((next_stage_2, next_state_2), value_2),
        ...
    ]
) -> optimal_value

f.select_max(
    (current_stage, current_state),
    [
        ((next_stage_1, next_state_1), value_1),
        ((next_stage_2, next_state_2), value_2),
        ...
    ]
) -> optimal_value

f.get_decisions_path(
    some_stage, some_state
) -> [(stage_1, state_1), (stage_2, state_2), ...]
```

### Example

`examples/descriptive.py` illustrates the usage of `descriptive_dp`. It implements two DP-function `renew_equipment` and `renew_equipment_no_store` to solve equipment_renewal problem, with or without storing the decisions path.

Enter `python3 examples/descriptive.py` to run the program. If you want to see detailed logging, set environment variable `LOGLEVEL` to `DEBUG` like this: `LOGLEVEL=DEBUG python3 examples/descriptive.py`.
