# encoding: utf-8

"""
@ filename: bootstrap.py
@ author  : c0rpse
"""

from Access.Auth import Auth
from Access.Search import Search
from config import ZoomEye_Username, ZoomEye_Password, ZoomEye_AuthPath
import pprint
if __name__ == '__main__':
    auth = Auth(ZoomEye_AuthPath, ZoomEye_Username, ZoomEye_Password)
    auth.get_access_token()
    if auth.access_error is False:
        srh = Search(auth.access_token)
        srh.gen_search_header()
        srh.gen_search_rest('zabbix')
        srh.execute_search()
        pprint.pprint( srh.result)
