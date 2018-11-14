import numbers
import operator
import functools

import logging

logger = logging.getLogger(__name__)


def _select(args, *, method='max', store_decisions=True):
    """
    args: List[((next_stage, next_state), value)]

    returns:
    `((next_stage, next_state), optimized_value)` if `store_decisions == True`;
    `optimized_value` only otherwise.
    """

    use_max = method == 'max'

    if store_decisions:
        assert all(
            isinstance(x, tuple) and len(x) == 2 and isinstance(x[1], numbers.Real)
            for x in args
        )
    else:
        assert all(
            isinstance(x, numbers.Real)
            for x in args
        )

    if store_decisions:

        best = (None, float('-inf') if use_max else float('inf'))
        cmp = operator.ge if use_max else operator.le
        for item in args:
            if cmp(item[1], best[1]):
                best = item

        return best

    else:

        f = max if use_max else min
        return f(args)


class dp:

    def __init__(self, store_decisions=True):

        self.__store_decisions = store_decisions
        self.__state_target_mapping = {}  # Mapping: (stage, state) -> cost

        if self.__store_decisions:
            self.__state_transfer_mapping = {}  # Mapping: (stage, state) -> (next_stage, next_state)

    def select(self, *arguments, method=None):

        if self.__store_decisions:
            current, args = arguments
        else:
            args = arguments[0]

        result = _select(args, method=method, store_decisions=self.__store_decisions)

        if self.__store_decisions:
            next_, next_value = result
            self.__state_transfer_mapping[current] = next_
            return next_value
        else:
            return result

    def __call__(self, func):
        """
        func: Callable[stage, current_state] -> maximum earnings / minimum costs
        """

        @functools.wraps(func)
        def _wrapped(stage, state):

            current = (stage, state)
            if current in self.__state_target_mapping:
                value = self.__state_target_mapping[current]
                logger.debug('{}({}, {}) hits cache: {}'.format(func.__name__, stage, state, value))
                return value

            logger.debug('{}({}, {}) not computed'.format(func.__name__, stage, state))

            value = func(stage, state)
            self.__state_target_mapping[current] = value

            return value

        _wrapped.select_min = functools.partial(self.select, method='min')
        _wrapped.select_max = functools.partial(self.select, method='max')
        _wrapped.get_decisions_path = self.get_decisions_path
        return _wrapped

    def get_decisions_path(self, stage, state):

        if not self.__store_decisions:
            raise NotImplementedError

        current_ = (stage, state)
        if current_ not in self.__state_transfer_mapping:
            raise RuntimeError("State {!r} not yet reached.".format(current_))

        path = [current_]
        while True:

            next_ = self.__state_transfer_mapping.get(current_, None)
            if next_ is None:
                break
            else:
                path.append(next_)

            current_ = next_

        return path
