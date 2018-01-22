#!/bin/python
# -*- coding: utf-8 -*-

import sys
import os 
import unittest

sys.path.append(os.path.join(os.getcwd(), ".."))
import seedfile_load

class SeedLoadTestcase(unittest.TestCase):
    """Unittest class for seedfile_load module.

    Attributes:
        seed_file:  Name of seed file.
        urls:       Urls list
    """

    def setUp(self):
        self.seed_file = "../urls"
        self.urls = seedfile_load.seedfile_load(self.seed_file)

    def test_seed_load(self):
        urls = ["http://www.baidu.com"]
        self.assertEqual(self.urls, urls)


if __name__ == "__main__":
    unittest.main()
