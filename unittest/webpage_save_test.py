#!/bin/python
# -*- coding: utf-8 -*-

import sys
import os 
import urllib
import unittest

sys.path.append(os.path.join(os.getcwd(), ".."))
import webpage_save

class WebSaveTestcase(unittest.TestCase):
    """Unittest class for webpage_save module.

    Attributes:
        content:        HTML content.
        url:            Source url of the content.
    """

    def setUp(self):
        self.url = "http://www.baidu.com"
        self.content = ("<a href='http://news.baidu.com'>Baidu news</a>"
        "<a href='http://images.baidu.com'>Baidu images</a>"
        "<a href='javascript:location.href=\"test.html\"'>Test</a>")
        self.output = "./output"
        self.fname = urllib.quote_plus(self.url)

    def test_webpage_save(self):
        res = webpage_save.save_file(self.content, self.url, self.output)
        self.assertEqual(res, None)
        self.assertTrue(os.path.exists(self.output + '/' + self.fname))

if __name__ == "__main__":
    unittest.main()
