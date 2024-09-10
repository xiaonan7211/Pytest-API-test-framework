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


case_id = ['get_plantemplate_all', 'get_plantemplate_all_status', 'get_plantemplate_all_size3', 'get_plantemplate_all_gradeId', 'get_plantemplate_all_catalogId', 'get_plantemplate_all_name', 'get_plantemplate_all_combination', 'get_plantemplate_all_error_catalogId', 'get_plantemplate_all_error_status', 'get_plantemplate_all_error_name', 'get_plantemplate_all_error_gradeId']
TestData = GetTestCase.case_data(case_id)
re_data, str_redata = regular(TestData)


@allure.epic("Gymery")
@allure.feature("计划模板服务")
class TestPlantemplateAll:
    
    @allure.story("查询计划模板列表")
    @pytest.mark.PlanTemplate
    @pytest.mark.parametrize('in_data', eval(str_redata), ids=[i['detail'] for i in re_data])
    def test_plantemplate_all(self, in_data, case_skip):
        """
        :param :
        :return:
        """
        res = RequestControl(in_data).http_request()
        TearDownHandler(res).teardown_handle()
        Assert(in_data['assert_data']).assert_equality(response_data=res.response_data,
                                                       sql_data=res.sql_data, status_code=res.status_code)


if __name__ == '__main__':
    pytest.main(['test_plantemplate_all.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
