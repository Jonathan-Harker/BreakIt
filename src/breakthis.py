import itertools
from inspect import signature


class BreakThis:
    def __init__(self, expected_exception: type(BaseException), function):
        self.expected_exception = expected_exception
        self.function = function

    def break_with_primitive_zero_types(self):
        arg_list = self.get_arg_list()

        broken_cases = []
        for args in arg_list:
            try:
                self.function(*args)
            except self.expected_exception:
                pass
            except Exception:
                broken_cases.append(args)

        return broken_cases

    def get_arg_list(self):
        no_args = self.get_no_args()
        params = [0, 0.0, False, "", [], {}, None]
        arg_list = self.build_arg_list(no_args, params)
        return arg_list

    def build_arg_list(self, no_args, params):
        arg_list = []

        for i in range(no_args):
            arg_list.append(params)

        return list(itertools.product(*arg_list))


    def get_no_args(self):
        details = signature(self.function)
        no_args = len(details.parameters)
        return no_args
