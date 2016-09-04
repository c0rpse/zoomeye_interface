# encoding: utf-8

"""
@ filename: config.py
@ author  : c0rpse
"""
from config import ZoomEye_AccessAuth, ZoomEye_AccessType, ZoomEye_SearchWebPath, ZoomEye_SearchHostPath
from utils import urlencode, http_req


class Search(object):

    def __init__(self, token):
        self.access_token = token
        self.access_header = None
        self.query = None
        self.facets = None
        self.page = 1
        self.rest = None
        self.result = None
        self.access_url = None

    def gen_search_header(self):
        self.access_header = [
            ':'.join([ZoomEye_AccessAuth, ZoomEye_AccessType+' '+self.access_token])
        ]

    def gen_search_rest(self, query, page=1, facets='app,os'):
        if query is not None:
            if isinstance(query, dict):
                self.query = '%20'.join([':'.join([str(i), query[i]]) for i in query])
            else:
                self.query = query
        if page:
            self.page = page
        if facets:
            self.facets = facets
        print self.query
        self.rest = urlencode({'query': self.query, 'page': self.page})

    def execute_search(self, s_type='web'):
        if s_type == 'web':
            self.access_url = '?'.join([ZoomEye_SearchWebPath, self.rest])
        elif s_type == 'host':
            self.access_url = '?'.join([ZoomEye_SearchHostPath, self.rest])

        response = http_req(self.access_url, 'GET', self.access_header)
        self.result = response







