#!/bin/python
# -*- coding: utf-8 -*-

import ConfigParser
import logging

class SpiderConf(object):
    """Class to store config info.

    Attributes:
        url_list_file:  The seed file which stores the request url list.
        output_directory:   The output data dir.
        max_depth:          The max crawl depth from the root url.
        crawl_interval:     The crawl request interval value.
        crawl_timeout:      The crawl request timeout value
        target_url:         The regex expression to store target url.
        thread_count:       The count limit for multi-threadings.
    """

    def __init__(self):
        self.url_list_file = "./urls"
        self.output_directory = "./output"
        self.max_depth = 5
        self.crawl_interval = 1
        self.crawl_timeout = 1
        self.target_url = ".*\.(html|gif|png|jpg|bmp)$"
        self.thread_count = 8

    def conf_parse(self, conf):
        """Config parser"""
        conf_parser = ConfigParser.ConfigParser()
        try:
            conf_parser.read(conf)
        except ConfigParser.Error as e:
            logging.error("Fail to load conf(%s) as ConfigParser.Error: %s", conf, e)
            return "Fail"
        try:
            self.url_list_file = conf_parser.get("spider", "url_list_file")
            self.output_directory = conf_parser.get("spider", "output_directory")
            self.max_depth = int(conf_parser.get("spider", "max_depth"))
            self.crawl_interval = int(conf_parser.get("spider", "crawl_interval"))
            self.crawl_timeout = int(conf_parser.get("spider", "crawl_timeout"))
            self.target_url = conf_parser.get("spider", "target_url")
            self.thread_count = int(conf_parser.get("spider", "thread_count"))
        except Exception as e:
            logging.error("Fail to parse conf as Exception:%s", e)
        return None
