# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import logging

import logging.config


if __name__=='__main__':

    logging.config.fileConfig("logger.conf")


    logger = logging.getLogger("demo1")

    logger.debug("这是demo1 debug日志记录")

    logger.info("这是demo1 info日志记录")

    logger.warning("这是demo1 warning日志记录")


