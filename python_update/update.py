import pip
from subprocess import call
for package in pip.get_installed_distributions():
   call('pip install --upgrade ' + package.project_name + " -i https://pypi.tuna.tsinghua.edu.cn/simple")
