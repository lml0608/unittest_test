# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import logging

import sys

#获取logger实例，参数为空是root logger
logger = logging.getLogger()


#指定logger输出格式

formatter = logging.Formatter("%(asctime)s %(levelname)-8s: %(message)s")

#文件日志
file_handler = logging.FileHandler("test.log")
#指定输出格式
file_handler.setFormatter(formatter)

#控制台日志
console_handler = logging.StreamHandler(sys.stdout)

console_handler.formatter = formatter

#为logger添加日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

#指定日志的最低输出级别。默认为warn
logger.setLevel(logging.INFO)

# 输出不同级别的log
logger.debug('this is debug info')
logger.info('this is information')
logger.warning('this is warning message')
logger.error('this is error message')
logger.fatal('this is fatal message, it is same as logger.critical')
logger.critical('this is critical message')


#移除一些日志处理器

logger.removeHandler(file_handler)

