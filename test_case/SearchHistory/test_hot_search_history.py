#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2022-11-21 11:53:40


import allure
import pytest
from utils.read_files_tools.get_yaml_data_analysis import GetTestCase
from utils.assertion.assert_control import Assert
from utils.requests_tool.request_control import RequestControl
from utils.read_files_tools.regular_control import regular
from utils.requests_tool.teardown_control import TearDownHandler


case_id = ['get_hot_search_history']
TestData = GetTestCase.case_data(case_id)
re_data, str_redata = regular(TestData)


@allure.epic("Gymery")
@allure.feature("搜索服务")
class TestHotSearchHistory:
    
    @allure.story("获取热门搜索接口")
    @pytest.mark.SearchHistory
    @pytest.mark.parametrize('in_data', eval(str_redata), ids=[i['detail'] for i in re_data])
    def test_hot_search_history(self, in_data, case_skip):
        """
        :param :
        :return:
        """
        res = RequestControl(in_data).http_request()
        TearDownHandler(res).teardown_handle()
        Assert(in_data['assert_data']).assert_equality(response_data=res.response_data,
                                                       sql_data=res.sql_data, status_code=res.status_code)


if __name__ == '__main__':
    pytest.main(['test_hot_search_history.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
