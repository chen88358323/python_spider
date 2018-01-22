#!/bin/python
# -*- coding: utf-8 -*-

import HTMLParser
import urlparse
import logging
import re

class MyParser(HTMLParser.HTMLParser):
    """Class to parse HTML content.

    Attributes:
        links:  List to store all links of the content.
        scheme: Request scheme of the url.
        host:   Host of the url request.
        src_url:Source url of the request.

    Raises:
        HTMLParseError: error occurred with HTMLParser
    """

    def __init__(self, scheme, host, src_url):
        HTMLParser.HTMLParser.__init__(self)
        self.links = []
        self.scheme = scheme
        self.host = host
        self.src_url = src_url

    def handle_starttag(self, tag, attrs):
        if tag == "a" or tag == "img":
            if len(attrs) == 0: pass
            else:
                for (k, v) in attrs:
                    if k == "href" or k == "src":
                        new_url = self.join_url(self.src_url, v)
                        if new_url != "":
                            self.links.append(new_url)

    def join_url(self, src_url, new_url):
        """
        join_url - Function to join two urls.

        Args:
            src_url:    The source url.
            new_url:    The new url(need to be joind)

        Returns:
            url:        The url after joind src and new url.
        """

        new_parse = urlparse.urlparse(new_url)
        new_scheme = new_parse.scheme
        new_loc = new_parse.netloc
        new_path = new_parse.path

        if new_loc == "":
            if new_scheme == "javascript":
                script_reg = re.compile(r'''location\.href=['|"](.*?)['|"]''')
                match = script_reg.match(new_path)
                if match:
                    url = urlparse.urljoin(src_url, match.group(1))
                else:
                    url = ""
            else:
                url = urlparse.urljoin(src_url, new_path)
        elif new_scheme == "":
            url = "http:" + new_url
        else:
            url = new_url
        return url
        

def webpage_parse(content, src_url):
    """
    webpage_parse - parse html content to find all urls.

    Args:
        content:    the html content to be parsed.
        src_url:    the source url of the content.

    Returns:
        urls:       All sub-urls in the content 
    """
    # get the current scheme
    urlparser = urlparse.urlparse(src_url)
    src_url_scheme = urlparser.scheme
    src_url_netloc = urlparser.netloc

    # get all the sub href links
    try:
        myparser = MyParser(src_url_scheme, src_url_netloc, src_url)
        myparser.feed(content)
        myparser.close()
        logging.info('Get all sub urls succ of : %s ', src_url)
    except HTMLParseError as e:
        logging.error("Fail to parse HTML for url(%s) as Exception: %s", src_url, e)

    return myparser.links
