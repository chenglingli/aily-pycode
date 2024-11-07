import requests
import json
from _sys import logger

def main(plugin_id, plugin_secret):
    ## 获取 token 的相关设置
    token_url = 'https://project.feishu.cn/open_api/authen/plugin_token'
    token_data = {
        "plugin_id": plugin_id,
        "plugin_secret": plugin_secret
    }
    token_headers = {
        "Content-Type": "application/json"
    }
    token_response = requests.post(token_url, headers=token_headers, data=json.dumps(token_data))
    
    ## 解析数据
    token_resp_json = token_response.json()
    token = token_resp_json['data']['token']

    ## 返回结果
    return token

