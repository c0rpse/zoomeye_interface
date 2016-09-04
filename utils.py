# encoding: utf-8

"""
@ filename: utils.py
@ author  : c0rpse
"""

import urllib2
import urllib
import pycurl
import StringIO
from config import Http_UserAgent

class ZoomEyeException(Exception):
    def __init__(self, code):
        self.code = code


def http_get(url, timeout=None, headers=None):
    request = urllib2.Request(url)
    # if set timeout
    if timeout and timeout.isdigit() and timeout > 0:
        urllib2.socket.setdefaulttimeout(timeout)

    # if set headers
    if headers is not None and isinstance(headers, dict):
        [request.add_header(h, headers[h]) for h in headers]

    return urllib2.urlopen(request)


def http_req(url, rtype="GET", headers=None, payloads=None):
    crl = pycurl.Curl()
    crl.setopt(pycurl.VERBOSE, 1)
    crl.setopt(pycurl.FOLLOWLOCATION, 1)
    crl.setopt(pycurl.MAXREDIRS, 3)

    crl.setopt(pycurl.CONNECTTIMEOUT, 60)
    crl.setopt(pycurl.TIMEOUT, 300)
    crl.setopt(pycurl.CUSTOMREQUEST, rtype)
    crl.setopt(pycurl.HTTPPROXYTUNNEL, 1)
    crl.fp = StringIO.StringIO()
    crl.setopt(pycurl.USERAGENT, Http_UserAgent)
    if rtype == "POST" and payloads is not None:
        crl.setopt(crl.POSTFIELDS, payloads)
    if headers is not None and isinstance(headers, list):
        # crl.setopt(pycurl.HEADER, True)
        crl.setopt(crl.HTTPHEADER, headers)
    crl.setopt(pycurl.URL, url)
    crl.setopt(crl.WRITEFUNCTION, crl.fp.write)
    crl.perform()
    response = crl.fp.getvalue()
    crl.fp.close()
    crl.close()
    return response


def urlencode(s):
    return urllib.urlencode(s)
