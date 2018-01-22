#!/bin/python
# -*- coding: utf-8 -*-

import sys
import os 
import urllib2
import unittest

sys.path.append(os.path.join(os.getcwd(), ".."))
import webpage_parse

class WebParseTestcase(unittest.TestCase):
    """Unittest class for webpage_parse module.

    Attributes:
        content:        HTML content.
        url:            Source url of the content.
        sub_urls:       Sub url list int the content
    """

    def setUp(self):
        self.url = "http://www.baidu.com"
        self.content = ("<a href='http://news.baidu.com'>Baidu news</a>"
        "<a href='http://images.baidu.com'>Baidu images</a>"
        "<a href='javascript:location.href=\"test.html\"'>Test</a>")
        self.sub_urls = ["http://news.baidu.com", "http://images.baidu.com", \
        "http://www.baidu.com/test.html"]

    def test_webpage_parse(self):
        urls = webpage_parse.webpage_parse(self.content, self.url)
        self.assertEqual(urls, self.sub_urls)


if __name__ == "__main__":
    unittest.main()
