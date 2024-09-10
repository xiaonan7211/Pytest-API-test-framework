#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2022-11-21 11:53:39


import allure
import pytest
from utils.read_files_tools.get_yaml_data_analysis import GetTestCase
from utils.assertion.assert_control import Assert
from utils.requests_tool.request_control import RequestControl
from utils.read_files_tools.regular_control import regular
from utils.requests_tool.teardown_control import TearDownHandler


case_id = ['get_all_actions_01', 'get_all_actions_null_02', 'get_all_actions_keyword_03', 'get_all_actions_keyword_delName']
TestData = GetTestCase.case_data(case_id)
re_data, str_redata = regular(TestData)


@allure.epic("Gymery")
@allure.feature("动作服务")
class TestAllActions:
    
    @allure.story("获取全部动作")
    @pytest.mark.Action
    @pytest.mark.parametrize('in_data', eval(str_redata), ids=[i['detail'] for i in re_data])
    def test_all_actions(self, in_data, case_skip):
        """
        :param :
        :return:
        """
        res = RequestControl(in_data).http_request()
        TearDownHandler(res).teardown_handle()
        Assert(in_data['assert_data']).assert_equality(response_data=res.response_data,
                                                       sql_data=res.sql_data, status_code=res.status_code)


if __name__ == '__main__':
    pytest.main(['test_all_actions.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
