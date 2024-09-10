#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Software: PyCharm

"""
异常类自定义
"""

import re
import logging
import six

# from werkzeug.exceptions import HTTPException

LOG = logging.getLogger(__name__)


class Error(Exception):
    """ERROR异常基类"""


class GyMeraTesteException(Error):
    """Base GyMeraTest Exception
    To correctly use this class, inherit from it and define
    a 'message' property. That message will get printf'd
    with the keyword arguments provided to the constructor.
    """
    message = "An unknown exception occurred."
    code = 500
    headers = {}
    safe = False

    def __init__(self, message=None, **kwargs):
        self.kwargs = kwargs

        if "code" not in kwargs:
            try:
                self.kwargs["code"] = self.code
            except AttributeError:
                LOG.exception("GyMeraTesteException 缺少属性 code")
                raise AttributeError
        for k, value in self.kwargs.items():
            if isinstance(value, Exception):
                self.kwargs[k] = six.text_type(value)

        if not message:
            try:
                message = self.message % kwargs
            except (ValueError, AttributeError, TypeError, NameError,):
                # kwargs doesn't match a variable in the message
                # log the issue and the kwargs
                LOG.exception('Exception in string format operation.')
                for name, value in kwargs.items():
                    LOG.error("%(name)s: %(value)s", {
                        'name': name, 'value': value})
                raise AttributeError

        elif isinstance(message, Exception):
            message = six.text_type(message)

        if re.match(r".*[^\.]\.\.$", message):
            message = message[:-1]
        self.msg = message
        super(GyMeraTesteException, self).__init__(message)


class GetSettingsException(GyMeraTesteException):
    """获取配置信息异常"""
    message = "获取配置信息异常 error：%(error)s | settingsFilePath： %(filepath)s"


class GetTokenException(GyMeraTesteException):
    """获取token异常"""
    message = "初始化获取token异常 error：%(error)s.  data：%(data)s"


class OpenTestCaseExcelException(GyMeraTesteException):
    """初始化时打开用例文件获取用例数据异常"""
    message = "初始化时打开用例文件获取用例数据异常  error：%(error)s"


class ExpectedDiscrepancyException(GyMeraTesteException):
    """接口执行失败异常"""
    message = "预期结果与实际结果不一致  error：%(error)s \n data: %(data)s \n url: %(url)s \n res: %(res)s"


class DataConversionExecution(GyMeraTesteException):
    """数据转换失败，请检查数据"""
    message = "数据转换失败，请检查数据  error：%(error)s \n data: %(data)s"


class WorkbookInexIstenceError(GyMeraTesteException):
    """工作表不存在"""
    message = "工作表不存在, 请检查工作表 error：%(error)s.  data: %(data)s"


class ApiOnFailureError(GyMeraTesteException):
    """接口执行时报错"""
    message = "接口执行时报错，请检查  error：%(error)s."


class AcquisitionDependencyFailed(GyMeraTesteException):
    """获取依赖失败"""
    message = "获取接口依赖失败 请检查依赖接口执行结果  依赖接口名称 error：%(error)s."


class SQLParsingFailedError(GyMeraTesteException):
    """获取依赖失败"""
    message = "SQL解析失败，请检查SQL格式 error：%(error)s.  "


class DataQueryException(GyMeraTesteException):
    """获取依赖失败"""
    message = "数据查询异常，请检查SQL error：%(error)s.  SQL：%(SQL)s."


class ReqObjectError(GyMeraTesteException):
    """request object is None or error"""
    message = ""


if __name__ == '__main__':
    pass
