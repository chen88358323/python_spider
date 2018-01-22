#!/bin/python
# -*- coding: utf-8 -*-

import sys
import os 
import unittest

sys.path.append(os.path.join(os.getcwd(), ".."))
import config_load

class ConfLoadTestcase(unittest.TestCase):
    """Unittest class for config_load module.

    Attributes:
        conf:           Name of config file.
        spider_conf:    Object of SpiderConf
    """

    def setUp(self):
        self.conf = "../spider.conf"
        self.spider_conf = config_load.SpiderConf()
        self.spider_conf.conf_parse(self.conf)

    def test_conf_parse(self):
        self.assertEqual(self.spider_conf.url_list_file, "./urls")
        self.assertEqual(self.spider_conf.output_directory, "./output")
        self.assertEqual(self.spider_conf.max_depth, 1)
        self.assertEqual(self.spider_conf.crawl_interval, 1)
        self.assertEqual(self.spider_conf.crawl_timeout, 5)
        self.assertEqual(self.spider_conf.target_url, ".*\.(gif|png|jpg|bmp)$")
        self.assertEqual(self.spider_conf.thread_count, 8)


if __name__ == "__main__":
    unittest.main()
