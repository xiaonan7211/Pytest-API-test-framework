#!/usr/bin/env python
# -*- coding: utf-8 -*-


from utils.logging_tool.log_control import INFO
import subprocess
import socket
import locale


def get_encoding():
    """获取当前系统编码"""
    return locale.getpreferredencoding()


def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    _s = None
    try:
        _s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _s.connect(('8.8.8.8', 80))
        l_host = _s.getsockname()[0]
    finally:
        _s.close()

    return l_host


def execute_cmd(command):
    """执行系统命令"""
    subp = subprocess.run(command,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         encoding=get_encoding())
    if subp.returncode == 0:
        INFO.logger.info(subp.stdout)
    else:
        INFO.logger.info(subp.stderr)
        raise Exception(subp.stderr)


if __name__ == '__main__':
    print(get_host_ip())
