# encoding: utf-8

"""
@ filename: config.py
@ author  : c0rpse
"""

from utils import http_req
from config import ZoomEye_AccessToken
import json


class Auth(object):

    def __init__(self, auth_path, auth_username, auth_password):
        self.auth_path = auth_path
        self.auth_username = auth_username
        self.auth_password = auth_password
        self.access_token = None
        self.access_token_json = None
        self.access_begin = False
        self.access_error = False
        self.access_error_info = None

    def gen_access_payload(self):
        return json.dumps({
            "username": self.auth_username,
            "password": self.auth_password
        })

    def gen_access_header(self):
        return []

    def get_access_token(self):
        if self.access_begin is True:
            self.access_error_info = None
            self.access_error = False

        try:
            self.access_token_json = http_req(
                self.auth_path,
                'POST',
                self.gen_access_header(),
                self.gen_access_payload()
            )
        except Exception:
            self.access_error = True

        if self.access_begin is False:
            self.access_begin = True
        self.access_error = False
        if self.access_error is False and self.access_token_json is not None:
            token = json.loads(self.access_token_json)
            if ZoomEye_AccessToken in token:
                self.access_token = token[ZoomEye_AccessToken]
            elif 'error' in token:
                self.access_error_info = token

    def get_error(self):
        if self.access_error:
            return self.access_error







