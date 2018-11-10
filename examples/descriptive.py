#!/usr/bin/env python3

import os

import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import logging

logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO'))

from descriptive_dp import dp

# r = [20000, 19000, 18500, 17200, 15500, 14000, 12000]
# c = [200, 600, 1200, 1500, 1700, 1800, 2200]
# s = [None, 80000, 60000, 50000, 30000, 10000, 5000]
# l = 100000  # noqa
# N = 5

r = [0] * 6
c = [30, 40, 50, 75, 90, float('inf')]
s = [None, 50, 25, 10, 5, 2]
p = [None, 100, 105, 110, 115, 120]
N = 5


@dp(True)
def renew_equipment(i, t):

    if i == N + 1:
        return 0

    if t > 5:
        return float('-inf')

    return renew_equipment.select_max(
        (i, t),
        [
            (
                (i + 1, t + 1),
                r[t] - c[t] + renew_equipment(i + 1, t + 1)
            ),
            (
                (i + 1, 1),
                r[0] - c[0] + s[t] - p[i] + renew_equipment(i + 1, 1)
            )
        ]
    )


@dp(False)
def renew_equipment_no_store(i, t):

    if i == N + 1:
        return 0

    if t > 5:
        return float('-inf')

    return max(
        r[t] - c[t] + renew_equipment_no_store(i + 1, t + 1),
        r[0] - c[0] + s[t] - p[i] + renew_equipment_no_store(i + 1, 1),
    )


if __name__ == '__main__':

    print('---------- Test renew_equipment ----------')
    print('Minimal cost for a 2-year-old equipment:', renew_equipment(1, 2))

    print('Renewal strategy:')
    for year, age in renew_equipment.get_decisions_path(1, 2):
        print('Year =', year, ', Age =', age)

    print('---------- Test renew_equipment_no_store ----------')
    print('Minimal cost for a 2-year-old equipment:', renew_equipment_no_store(1, 2))
    print('Minimal cost for a 1-year-old equipment:', renew_equipment_no_store(1, 1))
