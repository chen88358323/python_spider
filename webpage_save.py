#!/bin/python
# -*- coding: utf-8 -*-


import urllib
import os
import logging

def save_file(content, url, output):
    """
    save_file - save the content to local file.

    Args:
        content:   Content date will be save to local file.
        url:       Source url of the content, which as file name.
        output:    Output path to save files.
    """

    fname = urllib.quote_plus(url)
    output_path = os.path.join(os.getcwd(), output)
    try:
        if not os.path.exists(output_path):
            os.mkdir(output_path)
    except os.error as e:
        logging.error("Fail to make output dir as Exception:%s", e)
        return "Fail"

    local_file = None
    try:
        local_file = open(os.path.join(output_path, fname), "w")
        local_file.truncate()
        local_file.write(content)
        logging.info("Success to save url(%s) to local file.", url)
    except IOError as e:
        logging.error("Failed to save url(%s) to local as Exception: %s.", url, e)
    finally:
        if local_file is not None:
            local_file.close()
    return None
