# # -*- encoding: utf-8 -*-
#
# import json
#
# import jsonpath
#
#
# ["train.seq", "left.force", "right.force", "left.length", "right.length", "left.force.mode", "right.force.mode"]
#
# a = {
#     "value": [
#         {
#             "plan": {
#                 "id": 11
#             },
#             "lesson": {
#                 "le": {
#                     "id": 999
#                 }
#             }
#         },
#         {
#             "plan": {
#                 "id": 22
#             },
#             "lesson": {
#                 "le": {
#                     "id": 555
#                 }
#             }
#         }
#     ]
# }
#
# print(jsonpath.jsonpath(a, "$.value[*].lesson.le.id"))
# import radar
# print(radar.random_date())
#
# import re
#
#
# a = "select * from aaa where ii=$json($.value)"
# print(re.findall(r"\$json\((.*?)\)", a))
# print(10000000000/140000/365)
# print(2022-195)
#
# datas = """
# {"code":0,"message":"获取用户最近训练动作列表成功","properties":null,"value":[{"id":null,"name":null,"avatarId":null,"trainTime":1664360388.870000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664360388.838000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664360388.091000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664360387.870000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664358519.742000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664357493.267000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664348130.040000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664348129.980000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664348129.387000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664332371.726000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664277805.435000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664277805.390000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664276295.274000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664276164.587000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664276077.049000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664276039.486000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664275802.531000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664275548.221000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664275485.415000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664275308.706000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664275141.430000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664274341.603000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664274322.991000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664274211.795000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664274107.544000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664273889.591000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664273836.017000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664273645.480000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664273530.405000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664273480.326000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664273426.100000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664273411.581000000},{"id":null,"name":null,"avatarId":null,"trainTime":1664273170.128000000},{"id":"ACT22053018001400006003DC40095","name":"腰部拉伸","avatarId":"MTA2209081545120000100FF6B004C","trainTime":1663404204.933000000},{"id":"ACT22053018001400001003DC40095","name":"股二头肌拉伸","avatarId":"MTA2209081543520000100FF6BCC09","trainTime":1663401015.812000000},{"id":"ACT2208091423190003000E864005F","name":"仰卧抬腿","avatarId":"MTA2209081558160000100FF6B0045","trainTime":1663400992.218000000},{"id":"ACT2208091423190003100E864005F","name":"gymera侧屈","avatarId":"MTA2209081558250000100FF6B0049","trainTime":1663311891.769000000},{"id":"ACT2208091423190002600E864005F","name":"gymera腿弯举","avatarId":"MTA2209081557530000100FF6B004C","trainTime":1663311788.979000000},{"id":"ACT2208091423190003000E864005F","name":"仰卧抬腿","avatarId":"MTA2209081558160000100FF6B0045","trainTime":1663311630.932000000},{"id":"ACT2208091603440002100E864005E","name":"gymera耸肩","avatarId":"MTA2209081602440000100FF6B0049","trainTime":1663311335.387000000},{"id":"ACT2208091423190002200E864005F","name":"早安式前屈","avatarId":"MTA2209081557140000100FF6B004A","trainTime":1663311066.242000000},{"id":"ACT2208091423190002600E864005F","name":"gymera腿弯举","avatarId":"MTA2209081557530000100FF6B004C","trainTime":1663311001.600000000},{"id":"ACT22053018001400001003DC40095","name":"股二头肌拉伸","avatarId":"MTA2209081543520000100FF6BCC09","trainTime":1663310671.376000000},{"id":"ACT22053018001400001003DC40095","name":"股二头肌拉伸","avatarId":"MTA2209081543520000100FF6BCC09","trainTime":1663298571.932000000},{"id":"ACT22053018001400001003DC40095","name":"股二头肌拉伸","avatarId":"MTA2209081543520000100FF6BCC09","trainTime":1663296371.347000000},{"id":"ACT22053018001400004003DC40095","name":"臀部拉伸","avatarId":"MTA2209081544450000100FF6BCC09","trainTime":1661517413.522000000},{"id":"ACT2208091603440002900E864005E","name":"站姿gymera夹胸","avatarId":"MTA2209081603560000100FF6B0048","trainTime":1661347149.050000000},{"id":"ACT22053018533700004003EB80094","name":"卧姿滑轮卧推","avatarId":"MTA2208091452280000100084B002E","trainTime":1661339484.716000000},{"id":"ACT22053018001400006003DC40095","name":"腰部拉伸","avatarId":"MTA2209081545120000100FF6B004C","trainTime":1661311672.421000000},{"id":null,"name":null,"avatarId":null,"trainTime":1661164047.132000000},{"id":null,"name":null,"avatarId":null,"trainTime":1661163938.277000000}]}
# """
#
# datas = json.loads(datas)
# print(len(datas.get("value")))
# a = [12]
# c = [23]
# d = list(zip(a, c))
# print(d)
#
# a = [{"12": 12}]
# c = [{"13": 1300}, {"14": 14}, {"15": 15}]
#
# d = a + c
# print(d)
# from datetime import datetime
#
# def a():
#     print(datetime.now())
#     return datetime.now()
#
# nums = 31324564/5
# print(nums)
# if type(nums) == float:
#     nums = str(nums)
#     int(nums[:nums.find(".")]) + 1
#
# def paging(string: str):
#     nums = str(eval(string))
#     if int((nums[nums.find(".")+1:nums.find(".")+2])) != 0:
#         return int(nums[:nums.find(".")]) + 1
#     else:
#         return int(nums[:nums.find(".")])
#
# print(paging("250/70"))
#
# a = [None, 1, 0 , 1, 0]
# bool_list = list(map(bool, a))
# print(bool_list)
# s = [False, True, True, False,False]
# print(bool_list == s)
import json
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import traceback
import threading

# 发件人邮箱账号
sender = 'ganyuhao@gymera.net'
# user登录邮箱的用户名，password登录邮箱的密码（授权码，即客户端密码，非网页版登录密码），但用腾讯邮箱的登录密码也能登录成功
ssss = 'zhangyaguang@gymera.net'
password = 'Gyh3232489'

baidu_url = 'http://192.168.0.140:8000/#'

# def send_mail(mail_to, subject, content, sub_type='plain'):
#     ret = True
#     try:
#         # 邮件内容
#         msg = MIMEText(content, sub_type, 'utf-8')
#         # 括号里的对应发件人邮箱昵称、发件人邮箱账号
#         msg['From'] = formataddr([sender, sender])
#         # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#         msg['To'] = formataddr([mail_to, mail_to])
#         # 邮件的主题
#         msg['Subject'] = subject
#
#         # SMTP服务器，腾讯企业邮箱端口是465，腾讯邮箱支持SSL(不强制)， 不支持TLS
#         # qq邮箱smtp服务器地址:smtp.qq.com,端口号：456
#         # 163邮箱smtp服务器地址：smtp.163.com，端口号：25
#         server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
#         # 登录服务器，括号中对应的是发件人邮箱账号、邮箱密码
#         server.login(sender, password)
#         # 发送邮件，括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#         server.sendmail(sender, [mail_to, ], msg.as_string())
#         # 关闭连接
#         server.quit()
#         # 如果 try 中的语句没有执行，则会执行下面的 ret=False
#     except (Exception, ) as error:
#         print(error)
#     return ret
#
#
# def send_async_mail_prepare(user_name, user_password, user_email):
#     email_title = f'邮件主题-xxxxxx！'
#     content = f"尊敬的xxxxxx您好：<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;" \
#               f"这里是邮件的内容 xxxxxx， <br/><br/>" \
#               f"&nbsp;&nbsp;&nbsp;&nbsp;百度地址是：<a href='{baidu_url}'>Baidu</a>"
#     send_mail(user_email, email_title, content, "html")
#
import paramiko
import os
import sys


class Connection:

    def connect(self, ip, port, user, pwd):
        self.ip = ip
        self.port = port
        self.user = user
        self.pwd = pwd
        self.sshClient = paramiko.SSHClient()
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if pwd != '':
            self.sshClient.connect(ip, port, user, pwd)
        else:
            try:
                self.sshClient.connect(ip, port, user, pwd, look_for_keys=False, timeout=5.0)
            except paramiko.ssh_exception.AuthenticationException:
                self.sshClient.get_transport().auth_none(user)
        self.sftp = paramiko.SFTPClient.from_transport(self.sshClient.get_transport())

    def sftp_upload_whole_folder(self, local_folder, remote_folder):
        sftp = self.sftp
        root_path = None
        for path, dirs, files in os.walk(local_folder):
            root_path = path if root_path is None else root_path
            remote_path = path.replace(root_path, remote_folder)
            for d in dirs:
                try:
                    sftp.listdir(os.path.join(remote_path, d))
                except IOError:
                    sftp.mkdir(os.path.join(remote_path, d))
            for f in files:
                sftp.put(os.path.join(path, f), os.path.join(remote_path, f))
                print(os.path.join(path, f), os.path.join(remote_path, f))
        sftp.close()

    def push(self, local_file, remote_file):
        self.sftp.put(local_file, remote_file)

    def pull(self, remote_file, local_file):
        self.sftp.get(remote_file, local_file)

    def exe(self, cmd):
        try:
            a = self.sshClient.exec_command(cmd, timeout=60000)
            f_in, f_out, f_err = a
            return f_out.read().decode()
        except Exception as e:
            print(e)
            return 'Exception no return'

    def exe_invoke(self, cmd, end_str=None):
        """
        交互式执行命令，和exe实现功能相同。执行出错的时候可以尝试
        :param cmd:
        :param end_str: 通过该字段判断命令是否结束
        :param delaytime:
        :return:
        """
        try:
            ssh = self.sshClient.get_transport().open_session()
            ssh.get_pty()
            ssh.invoke_shell()
            ssh.send(cmd + '\n')
            ret = ""
            while True:
                out = ssh.recv(1024)
                # print(out.decode('utf-8'))
                ret = ret + out.decode('utf-8').replace('\r', '')
                if end_str in out.decode('utf-8'):
                    break
            return ret
        except Exception as e:
            log(e)
            return 'Exception no return'

    def exists(self, path):
        path_d = '/'.join(path.split('/')[:-1])
        path_b = path.split('/')[-1]
        print('---------')
        print(path_d)
        print(path_b)
        ls = self.exe('ls %s' % path_d).decode().split('\n')
        print(ls)
        if path_b in ls:
            return True
        else:
            return False

    def reconect(self):
        print('reconneting')
        try:
            self.close()
        except:
            pass
        finally:
            self.connect(self.ip, self.port, self.user, self.pwd)

    def close(self):
        self.sshClient.close()
        self.sftp.close()


import time
import subprocess
import locale


def cmd(command):
    subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            encoding=locale.getpreferredencoding())

    if subp.poll() == 0:
        print(subp.communicate()[0])
    else:
        out, err = subp.communicate()
        print(out, err)
        raise Exception(err)


def runcmd(command):
    ret = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         encoding=locale.getpreferredencoding())
    if ret.returncode == 0:
        print("success:", ret.stdout)
    else:
        print("error:", ret.stderr)


#     # send_async_mail_prepare('test', 'test', ssss)
#     print((16 + 18 + 20 + 12 + 12 + 11 + 15 + 12 + 11 + 15) * 15)
#     con = Connection()
# con.connect("192.168.0.140", 22, "root", "root")
# print(con.exe("mkdir /usr/report/html"))
# con.sftp_upload_whole_folder(r"D:\Project\test-server\report\html", "/usr/report")
# con.push(r"D:\来自谷歌的下载\git-2.9.0.tar.gz", "/usr/local/src/")
# con.exe("mkdir /usr/report/tmp")
# cmd(r"allure generate D:\Project\test-server\report\tmp -o D:\Project\test-server\report\html --clean")
# runcmd(r"allure generate D:\Project\test-server\report\tmp -o D:\Project\test-server\report\html --clean")

if __name__ == '__main__':
    # with open("ii.json", "r", encoding="utf-8") as f:
    #     data = json.load(f)
    #     print(list(map(lambda x: x.get("id"), data.get("value"))))
    #
        # print(len(data.get("value")))
    dt = "2022-10-31 03:00:00.000"
    tt = time.strptime(dt, "%Y-%m-%d %H:%M:%S.%f")
    print(time.mktime(tt))
    for i in range(1, 7, 2):
        print(i)
    s = [2, 3, 4,  5]
    print(s[1:3])

    a = """
站姿gymera夹胸
站姿gymera推胸
站姿gymera高位夹胸
站姿gymera低位夹胸
站姿gymera前推
站姿gymera屈肘夹胸
gymera正握手环弯举（24）
站姿反握二头弯举
坐姿gymera屈肘弯举1（33）
坐姿gymera屈肘弯举1（33）
gymera前平举（28）
仰卧gymera臂屈伸
仰卧gymera窄推（30）
站姿gymera臂屈伸（29）
gymera下压（6）
站姿gymera双手直臂下压（19）
单臂gymera下拉
gymera深蹲（12）
gymera弓步蹲（13）
gymera直腿硬拉（14）
俯卧gymera腿弯举（38）
站姿直腿gymera外展
屈髋屈膝外展
屈髋直腿gymera后伸
宽立深蹲
站姿gymera握杆提踵
坐姿gymera握杆提踵（40）
站姿对角线伐木
坐姿下拉侧屈
单腿站姿拉臂
坐姿gymera俄罗斯转体
gymera体侧屈
单腿站姿gymera推胸
gymera侧平举（23）
gymera屈臂外旋
站立屈肘上旋（25）
坐姿划船
仰卧gymera下拉（4）
坐姿gymera向上推（22）
坐姿颈后gymera下拉（3）
站姿gymera划船
站姿gymera宽握划船
gymera背飞鸟（17）
gymera肩胛后引
Y字型gymera手环伸展
站姿gymera下拉（1）
俯身gymera下拉
早安式前屈（42）
gymera下压（6）
站姿gymera下拉（1）
站姿反握二头弯举
gymera深蹲（12）
站姿gymera握杆提踵
坐姿gymera握杆提踵（40）
屈髋直腿gymera后伸
站姿gymera双手直臂下压（19）
坐姿gymera向上推（22）
早安式前屈（42）
站姿gymera高位夹胸
站姿gymera低位夹胸
坐姿颈后gymera下拉（3）
gymera正握手环弯举（24）
仰卧gymera窄推（30）
gymera下压（6）
站姿gymera双手直臂下压（19）
站姿对角线伐木
坐姿gymera俄罗斯转体
单腿站姿gymera推胸
gymera侧平举（23）
Y字型gymera手环伸展
俯身gymera下拉
早安式前屈（42）
"""

    b = """
gymera侧平举（23）
gymera屈臂外旋
站立屈肘上旋（25）
坐姿划船
仰卧gymera下拉（4）
坐姿gymera向上推（22）
坐姿颈后gymera下拉（3）
站姿gymera划船
站姿gymera宽握划船
gymera背飞鸟（17）
gymera肩胛后引
Y字型gymera手环伸展
站姿gymera下拉（1）
俯身gymera下拉
早安式前屈（42）
站姿gymera夹胸
站姿gymera推胸
站姿gymera高位夹胸
站姿gymera低位夹胸
站姿gymera前推
站姿gymera屈肘夹胸
gymera正握手环弯举（24）
站姿反握二头弯举
坐姿gymera屈肘弯举1（33）
坐姿gymera屈肘弯举1（33）
gymera前平举（28）
仰卧gymera臂屈伸
仰卧gymera窄推（30）
站姿gymera臂屈伸（29）
gymera下压（6）
站姿gymera双手直臂下压（19）
单臂gymera下拉
gymera深蹲（12）
gymera弓步蹲（13）
gymera直腿硬拉（14）
俯卧gymera腿弯举（38）
站姿直腿gymera外展
屈髋屈膝外展
屈髋直腿gymera后伸
宽立深蹲
站姿gymera握杆提踵
坐姿gymera握杆提踵（40）
站姿对角线伐木
坐姿下拉侧屈
单腿站姿拉臂
坐姿gymera俄罗斯转体
gymera体侧屈
单腿站姿gymera推胸
"""


    def difference(a, b):
        _b = set(b)
        return [item for item in a if item not in _b]

    c = list(set(b.split("\n")))
    d = a.split("\n")
    print(c)
    print(d)
    res = difference(d, c)
    print(res)
    # print(len(c)-1)
    print(len(set(a.split("\n")))-1)
    # from collections import Counter
    # print(Counter())














