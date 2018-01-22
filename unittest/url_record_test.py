#!/bin/python
# -*- coding: utf-8 -*-

import sys
import os 
import unittest

sys.path.append(os.path.join(os.getcwd(), ".."))
import url_record

class URLRecordTestcase(unittest.TestCase):
    """Unittest class for url_load module.

    Attributes:
        urls:        Test input urls list.
        known_url:   Test exsitent url.
        unknown_url: Test non-exsitent url.
    """

    def setUp(self):
        self.urls = ["http://news.baidu.com", "http://www.baidu.com", "http://www.baidu.com"]
        self.known_url = "http://www.baidu.com"
        self.unknown_url = "image.baidu.com"

    def test_url_record_put(self):
        for url in self.urls:
            url_record.url_record_put(url)
        self.assertEqual(len(url_record.url_record), 2)

    def test_url_record_get(self):
        for url in self.urls:
            url_record.url_record_put(url)
        self.assertEqual(url_record.url_record_get(self.known_url), self.known_url)
        self.assertEqual(url_record.url_record_get(self.unknown_url), None)


if __name__ == "__main__":
    unittest.main()
