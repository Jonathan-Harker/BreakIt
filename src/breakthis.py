import itertools
from inspect import signature


class BreakThis:
    def __init__(self, expected_exception: type(BaseException), function):
        self.expected_exception = expected_exception
        self.function = function
        self.broken_cases = []

    def breaker(self):
        self._break_with_primitive_zero_types()

    def _break_with_primitive_zero_types(self):
        arg_list = self._get_arg_list()

        for args in arg_list:
            try:
                self.function(*args)
            except self.expected_exception:
                pass
            except Exception:
                self.broken_cases.append(args)

    def _get_arg_list(self):
        no_args = self._get_no_args()
        params = [0, 0.0, False, "", [], {}, None]
        return self._build_arg_list(no_args, params)

    def _build_arg_list(self, no_args, params):
        arg_list = []

        for i in range(no_args):
            arg_list.append(params)

        return list(itertools.product(*arg_list))


    def _get_no_args(self):
        details = signature(self.function)
        no_args = len(details.parameters)
        return no_args
