#!/bin/python
# -*- coding: utf-8 -*-

import urllib2
import re
import logging

def webpage_urlopen(url, crawl_timeout):
    """
    webpage_urlopen - Function to get content from specific url.

    Args:
        url:            The source url to be request.
        crawl_timeout:  The request timeout value.

    Returns:
        content:        Response content of the urls. 
    """

    try:
        page = urllib2.urlopen(url, timeout = crawl_timeout)
        content = page.read()

        regex = ur'meta.*charset=("?)(.*?)("|>)'
        match = re.search(regex, content)
        html_charset = 'utf-8'  # default charset
        if match:
            html_charset = match.group(2)
        else:
            logging.warning("Fail to match charset Regex for url:%s, "
                "using the default charset.", url)
            return content

        if html_charset == "gb2312" or html_charset == "GBK":
            html_charset = "GB18030"
        elif html_charset == "iso-8859-1":
            html_charset = "latin-1"
        return content.decode(html_charset).encode("utf-8")
    except urllib2.HTTPError as e:
        if e.code == 403:
            logging.error("Fail to webpage_urlopen for url(%s) as "
                "HTTPError(403-Forbidden): %s", url, e)
        if e.code == 404:
            logging.error("Fail to webpage_urlopen for url(%s) as "
                "HTTPError(404-Not Found): %s", url, e)
        if e.code == 500:
            logging.error("Fail to webpage_urlopen for url(%s) as "
                "HTTPError(500-Internal Server Error): %s", url, e)
        else:
            logging.error("Fail to webpage_urlopen for url(%s) as "
                "HTTPError: %s", url, e)
    except urllib2.URLError as e:
        logging.error("Fail to webpage_urlopen for url(%s) as URLError: %s", url, e)
    except IOError as e:
        logging.error("Fail to webpage_urlopen for url(%s) as IOError: %s", url, e)
    except Exception as e:
        logging.error("Fail to webpage_urlopen for url(%s) as unknowException: %s", url, e)
    return ""
