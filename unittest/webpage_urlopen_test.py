#!/bin/python
# -*- coding: utf-8 -*-

import sys
import os 
import urllib2
import unittest

sys.path.append(os.path.join(os.getcwd(), ".."))
import webpage_urlopen

class WebSaveTestcase(unittest.TestCase):
    """Unittest class for webpage_urlopen module.

    Attributes:
        url:            Request url.
        timeout:        Timeout of the request
    """

    def setUp(self):
        self.url = "http://www.baidu.com"
        self.timeout = 5

    def test_webpage_save(self):
        content = webpage_urlopen.webpage_urlopen(self.url, self.timeout)
        self.assertIn("news", content)

if __name__ == "__main__":
    unittest.main()
