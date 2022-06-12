import unittest

from src.breakthis import BreakThis


def add(x, y):
    return x + y


class MyCustomException(BaseException):
    pass


class TestBreak(unittest.TestCase):
    def test__try_basic_types__returns_success_list(self):
        break_this = BreakThis(expected_exception=MyCustomException, function=add)
        break_this._break_with_primitive_zero_types()
        self.assertIsInstance(break_this.broken_cases, list)
        self.assertEqual(len(break_this.broken_cases), 38)

    def test_build_arg_list_builds_all_combinations(self):
        break_this = BreakThis(expected_exception=MyCustomException, function=add)
        params = ["p1", "p2"]
        arg_list = break_this._build_arg_list(no_args=3, params=params)
        self.assertEqual(len(arg_list), 8)
