#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""处理节点数据转换"""

import re


def jsonpath_replace(change_data, key_name, data_switch=None):
    """处理jsonpath数据
    ['$', 'data', 'videoAddReqs[0][1][2]', 'formatId[0]'] -->
    yaml_case.data["videoAddReqs"][0][1][2]["formatId"][0]
    """
    _new_data = key_name + ''
    for i in change_data:
        index_string = re.findall("\[.+]", i)
        if i == '$':
            pass
        elif data_switch is None and i == "data":
            _new_data += '.data'
        elif index_string:
            string = i.split(index_string[0])
            _new_data = _new_data + '[' + '"' + string[0] + '"' + ']'
            for y in index_string[-1]:
                if y == '[':
                    _new_data = _new_data + y
                elif y != '[' and y != ']':
                    _new_data = _new_data + y
                elif y == ']':
                    _new_data = _new_data + y
        else:
            _new_data = _new_data + '[' + '"' + i + '"' + ']'
    return _new_data


if __name__ == '__main__':
    a = jsonpath_replace(change_data=['$', 'data', 'id'], key_name='self.__yaml_case')
    print(a)