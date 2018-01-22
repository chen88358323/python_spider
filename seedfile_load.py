#!/bin/python
# -*- coding: utf-8 -*-

import urllib
import logging

def seedfile_load(seedfile):
    """
    seedfile_load - load crawl seed file.

    Args:
        seedfile:    The seed file will be loaded.
    Returns:
        urls:        All seed urls to be crawled.
    """

    urls = []
    try:
        with open(seedfile, "r") as f:
            for url in f.readlines():
                urls.append(url.strip())
            return urls
    except IOError as e:
        logging.error("Fail to load seedfile(%s) as Exception: %s", seedfile, e)
        return None
