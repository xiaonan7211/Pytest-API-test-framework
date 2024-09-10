#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Assert 断言类型
"""
import collections

from typing import Any, Union, Text


def paging_equals(
        check_value: Union[int, str],
        expect_value: Text,
        message: Text = ""
):
    """
    分页断言
    """
    nums = str(eval(expect_value))
    if int((nums[nums.find(".") + 1:nums.find(".") + 2])) != 0:
        expect_value = int(nums[:nums.find(".")]) + 1
    else:
        expect_value = int(nums[:nums.find(".")])
    assert int(check_value[0]) == expect_value, message


def calculate_equals(
        check_value: Union[int, str],
        expect_value: str,
        message: Text = ""
):
    """
    计算实际结果是否与预期结果相等
    """
    nums = str(eval(check_value))
    assert nums == str(expect_value), message


def bool_equals(
        check_value: Union[int, str, bool],
        expect_value: Union[int, str, bool],
        message: Text = ""
):
    """
    bool值断言
    """
    if isinstance(check_value, (int, str)):
        check_value = int(check_value)
        check_value = False if check_value == 0 else True
    if isinstance(expect_value, (int, str)):
        expect_value = int(expect_value)
        expect_value = False if expect_value == 0 or expect_value is None else True
    if isinstance(expect_value, list):
        assert check_value == expect_value, message
    else:
        assert check_value[0] == expect_value, message


def equals(
        check_value: Union[int, str, list], expect_value: Union[int, str, list], message: Text = ""
):
    """判断是否相等"""
    if isinstance(check_value, list) and isinstance(expect_value, list) and len(expect_value) != 0:
        check_value = list(map(lambda x: str(x), check_value))
        expect_value = list(map(lambda x: str(x), expect_value))
        assert collections.Counter(check_value) == collections.Counter(expect_value)

    elif isinstance(check_value, (str, int)):
        assert str(check_value) == str(expect_value), message
    elif check_value is None and expect_value is None:
        assert check_value == expect_value, message
    else:
        assert str(check_value[0]) == str(expect_value), message


def less_than(
        check_value: Union[int, float, list], expect_value: Union[int, float], message: Text = ""
):
    """判断实际结果小于预期结果"""
    assert check_value[0] < expect_value, message


def less_than_or_equals(
        check_value: Union[int, float, list], expect_value: Union[int, float], message: Text = ""):
    """判断实际结果小于等于预期结果"""
    assert check_value[0] <= expect_value, message


def greater_than(
        check_value: Union[int, float, list], expect_value: Union[int, float], message: Text = ""
):
    """判断实际结果大于预期结果"""
    assert check_value[0] > expect_value, message


def greater_than_or_equals(
        check_value: Union[int, float, list], expect_value: Union[int, float], message: Text = ""
):
    """判断实际结果大于等于预期结果"""
    assert check_value[0] >= expect_value, message


def not_equals(
        check_value: Any, expect_value: Any, message: Text = ""
):
    if isinstance(check_value, list) and isinstance(expect_value, list) and len(expect_value) != 0:
        assert set(expect_value) - set(check_value) != set()
        """判断是否相等"""
    elif isinstance(check_value, (str, int)) or check_value == None:
        assert check_value != expect_value, message
    else:
        assert check_value[0] != expect_value, message


def string_equals(
        check_value: Text, expect_value: Any, message: Text = ""
):
    """判断字符串是否相等"""
    assert check_value[0] == expect_value, message


def length_equals(
        check_value: Text, expect_value: int, message: Text = ""
):
    """判断长度是否相等"""
    if isinstance(expect_value, str):
        expect_value = int(expect_value)
    assert isinstance(
        expect_value, int
    ), "expect_value 需要为 int 类型"
    if isinstance(check_value, (list, tuple)):
        check_value_len = len(check_value)
        if check_value_len == 1 and check_value[0] == []:
            check_value_len = 0
        assert check_value_len == expect_value, message
    else:
        if isinstance(check_value, int):
            assert check_value == expect_value, message


def length_greater_than(
        check_value: Text, expect_value: Union[int, float], message: Text = ""
):
    """判断长度大于"""
    expect_value = int(expect_value)
    assert isinstance(
        expect_value, (float, int)
    ), "expect_value 需要为 float/int 类型"
    assert len(str(check_value)) > expect_value, message


def length_greater_than_or_equals(
        check_value: Text, expect_value: Union[int, float], message: Text = ""
):
    """判断长度大于等于"""
    expect_value = int(expect_value)
    assert isinstance(
        expect_value, (int, float)
    ), "expect_value 需要为 float/int 类型"
    assert len(check_value) >= expect_value, message


def length_less_than(
        check_value: Text, expect_value: Union[int, float], message: Text = ""
):
    """判断长度小于"""
    expect_value = int(expect_value)
    assert isinstance(
        expect_value, (int, float)
    ), "expect_value 需要为 float/int 类型"
    assert len(check_value) < expect_value, message


def length_less_than_or_equals(
        check_value: Text, expect_value: Union[int, float], message: Text = ""
):
    """判断长度小于等于"""
    expect_value = int(expect_value)
    assert isinstance(
        expect_value, (int, float)
    ), "expect_value 需要为 float/int 类型"
    assert len(check_value) <= expect_value, message


def contains(check_value: Any, expect_value: Any, message: Text = ""):
    """判断期望结果内容包含在实际结果中"""
    assert isinstance(
        check_value, (list, tuple, dict, str, bytes)
    ), "expect_value 需要为  list/tuple/dict/str/bytes  类型"
    assert expect_value in check_value, message


def contained_by(check_value: Any, expect_value: Any, message: Text = ""):
    """判断实际结果包含在期望结果中"""
    assert isinstance(
        expect_value, (list, tuple, dict, str, bytes)
    ), "expect_value 需要为  list/tuple/dict/str/bytes  类型"

    assert check_value in expect_value, message


def startswith(
        check_value: Any, expect_value: Any, message: Text = ""
):
    """检查响应内容的开头是否和预期结果内容的开头相等"""
    assert str(check_value).startswith(str(expect_value)), message


def endswith(
        check_value: Any, expect_value: Any, message: Text = ""
):
    """检查响应内容的结尾是否和预期结果内容相等"""
    assert str(check_value).endswith(str(expect_value)), message
