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

Enter `python3 examples/descriptive.py` to run the program.

```
Minimal cost for a 2-year-old equipment: -340
Renewal strategy:
Year = 1 , Age = 2
Year = 2 , Age = 3
Year = 3 , Age = 1
Year = 4 , Age = 2
Year = 5 , Age = 3
Year = 6 , Age = 4
---------- Test renew_equipment_no_store ----------
Minimal cost for a 2-year-old equipment: -340
Minimal cost for a 1-year-old equipment: -310
```

If you want to see detailed logging, set environment variable `LOGLEVEL` to `DEBUG` like this: `LOGLEVEL=DEBUG python3 examples/descriptive.py`.

```
---------- Test renew_equipment ----------
DEBUG:descriptive_dp.decorators:renew_equipment(1, 2) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(2, 3) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(3, 4) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(4, 5) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(5, 6) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(5, 1) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(6, 2) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(6, 1) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(4, 1) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(5, 2) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(6, 3) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(6, 1) hits cache: 0
DEBUG:descriptive_dp.decorators:renew_equipment(5, 1) hits cache: -40
DEBUG:descriptive_dp.decorators:renew_equipment(3, 1) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(4, 2) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(5, 3) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(6, 4) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(6, 1) hits cache: 0
DEBUG:descriptive_dp.decorators:renew_equipment(5, 1) hits cache: -40
DEBUG:descriptive_dp.decorators:renew_equipment(4, 1) hits cache: -90
DEBUG:descriptive_dp.decorators:renew_equipment(2, 1) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(3, 2) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(4, 3) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(5, 4) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(6, 5) not computed
DEBUG:descriptive_dp.decorators:renew_equipment(6, 1) hits cache: 0
DEBUG:descriptive_dp.decorators:renew_equipment(5, 1) hits cache: -40
DEBUG:descriptive_dp.decorators:renew_equipment(4, 1) hits cache: -90
DEBUG:descriptive_dp.decorators:renew_equipment(3, 1) hits cache: -165
Minimal cost for a 2-year-old equipment: -340
Renewal strategy:
Year = 1 , Age = 2
Year = 2 , Age = 3
Year = 3 , Age = 1
Year = 4 , Age = 2
Year = 5 , Age = 3
Year = 6 , Age = 4
---------- Test renew_equipment_no_store ----------
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(1, 2) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(2, 3) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(3, 4) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(4, 5) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(5, 6) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(5, 1) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(6, 2) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(6, 1) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(4, 1) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(5, 2) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(6, 3) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(6, 1) hits cache: 0
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(5, 1) hits cache: -40
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(3, 1) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(4, 2) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(5, 3) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(6, 4) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(6, 1) hits cache: 0
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(5, 1) hits cache: -40
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(4, 1) hits cache: -90
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(2, 1) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(3, 2) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(4, 3) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(5, 4) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(6, 5) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(6, 1) hits cache: 0
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(5, 1) hits cache: -40
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(4, 1) hits cache: -90
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(3, 1) hits cache: -165
Minimal cost for a 2-year-old equipment: -340
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(1, 1) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(2, 2) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(3, 3) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(4, 4) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(5, 5) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(6, 6) not computed
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(6, 1) hits cache: 0
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(5, 1) hits cache: -40
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(4, 1) hits cache: -90
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(3, 1) hits cache: -165
DEBUG:descriptive_dp.decorators:renew_equipment_no_store(2, 1) hits cache: -245
Minimal cost for a 1-year-old equipment: -310
```
