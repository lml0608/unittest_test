# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
import logging

#日志写进日志
logging.basicConfig(filename='example.log', level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%M %p')

logging.warning("user [alex] attempted wrong password more than 3 times")
logging.critical("server is down")

