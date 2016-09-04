# encoding: utf-8

"""
@ filename: const.py
@ author  : c0rpse
"""

# 主机识别请求字段
HostSearchPmt = {
    'query': {'need': True},
    'page': {'need': False},
    'facets': {'need': False}
    }
# 主机识别统计字段
HostSearchCountPmt = {
    'app': {'desc': '应用，设备等'},
    'device': {'desc': '设备类型'},
    'service': {'desc': '服务类型'},
    'os': {'desc': '操作系统'},
    'port': {'desc': '端口号'},
    'country': {'desc': '国家'},
    'city': {'desc': '城市'},
}
# 主机识别响应字段
HostSearchRespPmt = {
    'matches': {'desc': '结果集'},
    'facets': {'desc': '统计结果'},
    'total': {'desc': '结果总数'},
}
#