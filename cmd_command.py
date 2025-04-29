# coding=utf8

from subprocess import check_output
from subprocess import call

def wincmd(my_command):
    val= (check_output(my_command, shell=True))
    return val

def runcmdwindow(my_command):
    val = call("start cmd /K " + my_command, shell=True)
    return val
