#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import traceback
import pytest
from utils.other_tools.get_local_ip import execute_cmd
from utils.other_tools.models import NotificationType
from utils.other_tools.allure_data.allure_report_data import AllureFileClean
from utils.logging_tool.log_control import INFO
from utils.notify.wechat_send import WeChatSend
from utils.notify.ding_talk import DingTalkSendMsg
from utils.notify.send_mail import SendEmail
from utils.notify.lark import FeiShuTalkChatBot
from utils.other_tools.allure_data.error_case_excel import ErrorCaseExcel
from utils import config
from utils.read_files_tools.case_automatic_control import TestCaseAutomaticGeneration
from common.setting import root_path


def run():
    # 从配置文件中获取项目名称
    try:
        INFO.logger.info(
            """
                             _    _         _      _____         _
              __ _ _ __ (_)  / \\  _   _| |_ __|_   _|__  ___| |_
             / _` | '_ \\| | / _ \\| | | | __/ _ \\| |/ _ \\/ __| __|
            | (_| | |_) | |/ ___ \\ |_| | || (_) | |  __/\\__ \\ |_
             \\__,_| .__/|_/_/   \\_\\__,_|\\__\\___/|_|\\___||___/\\__|
                  |_|
                  开始执行{}项目...
                """.format(config.project_name)
        )

        # 测试报告数据存放路径
        report_path = os.path.abspath(os.path.join(root_path(), "report"))
        html_path = os.path.abspath(os.path.join(root_path(), "report/html"))
        tmp_path = os.path.abspath(os.path.join(root_path(), "report/tmp"))

        # 判断报告目录是否存在，不存在就创建
        if not os.path.exists(report_path):
            os.mkdir(report_path)
        if not os.path.exists(html_path):
            os.mkdir(html_path)
        if not os.path.exists(tmp_path):
            os.mkdir(tmp_path)

        # 判断现有的测试用例，如果未生成测试代码，则自动生成
        TestCaseAutomaticGeneration().get_case_automatic()

        """启动ActionTrain标签的用例"""
        # pytest.main(['-s', '-m', 'ActionTrain', '-W', 'ignore:Module already imported:pytest.PytestWarning',
        #              '--alluredir', './report/tmp', "--clean-alluredir"])

        # 启动所有用例
        pytest.main(['-s', '-W', 'ignore:Module already imported:pytest.PytestWarning',
                     '--alluredir', './report/tmp', "--clean-alluredir"])
        """
                   --reruns: 失败重跑次数
                   --count: 重复执行次数
                   -v: 显示错误位置以及错误的详细信息
                   -s: 等价于 pytest --capture=no 可以捕获print函数的输出
                   -q: 简化输出信息
                   -m: 运行指定标签的测试用例
                   -x: 一旦错误，则停止运行
                   --maxfail: 设置最大失败次数，当超出这个阈值时，则不会在执行测试用例
                    "--reruns=3", "--reruns-delay=2"
                   """

        # 生成测试报告
        execute_cmd(f"allure generate {tmp_path} -o {html_path} --clean")

        # 统计用例执行数据
        allure_data = AllureFileClean().get_case_count()

        # 通知消息路由配置
        notification_mapping = {
            NotificationType.DING_TALK.value: DingTalkSendMsg(allure_data).send_ding_notification,
            NotificationType.WECHAT.value: WeChatSend(allure_data).send_wechat_notification,
            NotificationType.EMAIL.value: SendEmail(allure_data).send_main,
            NotificationType.FEI_SHU.value: FeiShuTalkChatBot(allure_data).post

        }

        # 根据配置，发送通知消息
        if config.notification_type != NotificationType.DEFAULT.value:
            notification_mapping.get(config.notification_type)()

        if config.excel_report:
            ErrorCaseExcel().write_case()

        # os.system(f"allure serve ./report/tmp --h %s -port 8888" % get_host_ip())

    except Exception:
        # 如有异常，相关异常发送邮件
        e = traceback.format_exc()
        send_email = SendEmail(AllureFileClean.get_case_count())
        send_email.error_mail(e)
        raise


if __name__ == '__main__':
    run()
