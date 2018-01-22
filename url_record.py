#!/bin/python
# -*- coding: utf-8 -*-

import logging
import threading

url_record = set()
lock = threading.RLock()
def url_record_put(url):
    """
    url_record_put - Put new url record int to the set.

    Args:
        url:        The new url will be stored in the record.
    """

    with lock:
        url_record.add(url)


def url_record_get(url):
    """
    url_record_get - Get if the url exists in the record.

    Args:
        url:        The url to be confirmed if exists in the record.

    Returns:
        url value if exists in the record, else return None.
    """

    with lock:
        if url not in url_record:
            url = None
    return url
