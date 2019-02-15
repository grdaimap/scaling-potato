# -*- coding:utf-8 -*-
'''
尊重原作者，在他基础上加入pip升级和选择国内源
@Author  : Soner
@version :
@Time    : 2017/11/3/0003 15:11
@license : Copyright(C), Your Company
'''
import pip
# pip V10.0.0以上版本需要导入下面的包
from pip._internal.utils.misc import get_installed_distributions
from subprocess import call
from time import sleep

call("python -m pip install --upgrade pip ", shell=True)

for dist in get_installed_distributions():
    # 执行后，pip默认为Python3版本
    # 双版本下需要更新Python2版本的包，使用py2运行，并将pip修改成pip2
    call("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ --upgrade " + dist.project_name, shell=True)
