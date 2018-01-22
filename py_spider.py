#!/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import HTMLParser
import re
import urlparse
import threading
import ConfigParser
import argparse
import time
import logging
import sys

import logger
import config_load
import seedfile_load
import crawl_thread

if __name__ == "__main__":
    logger.init_log("./log/spider", level=logging.DEBUG)
    # Arguments parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="show current script version", \
        action="version", version="%(prog)s 1.0")
    parser.add_argument("-c", "--conf", help="set config file", required="true")
    args = parser.parse_args()
    if args.conf:
        conf = args.conf 
        logging.info("Success to read conf args : %s", conf)
    else:
        logging.error("Fail to read conf args")
        sys.exit(1)

    # Config parser
    spider_conf = config_load.SpiderConf()
    res = spider_conf.conf_parse(conf)
    if res is not None:
        logging.error("Fail to parse the config(%s)")
        sys.exit(1)
    logging.info('Success to parse the config.')

    # Seed file load
    urls = seedfile_load.seedfile_load(spider_conf.url_list_file)
    if urls is None:
        logging.error("Fail to load the urls seed. Check the log for more info")
        sys.exit(1)
    logging.info('Success to load the url seed.')

    # Multi-Threads crawl webpage
    crawl_thread.crawl_thread_control(urls, spider_conf)
    logging.info("Finish all the multi-threading crawl requests.")
