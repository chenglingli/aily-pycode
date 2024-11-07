import requests
import json
from _sys import logger

def main(union_id, plugin_id, plugin_secret):

    logger.info(union_id)

    # 获取 token 的相关设置
    token_url = 'https://project.feishu.cn/open_api/authen/plugin_token'
    token_data = {
        "plugin_id": plugin_id,
        "plugin_secret": plugin_secret
    }
    token_headers = {
        "Content-Type": "application/json"
    }
    token_response = requests.post(token_url, headers=token_headers, data=json.dumps(token_data))
    token_resp_json = token_response.json()
    token = token_resp_json['data']['token']

    # 获取用户详情接口
    user_query_url = 'https://project.feishu.cn/open_api/user/query'
    user_query_headers = {
        'X-PLUGIN-TOKEN': token,
        'Content-Type': 'application/json'
    }
    user_query_data = {
        "out_ids": [union_id]  # 使用输入参数 user_key
    }
    user_query_response = requests.post(user_query_url, headers=user_query_headers, data=json.dumps(user_query_data))
    user_query_resp_json = user_query_response.json()

    logger.info(user_query_resp_json)
    
    # 提取并返回 user_key
    user_key = user_query_resp_json['data'][0]['user_key'] if 'data' in user_query_resp_json and user_query_resp_json['data'] else None
    return user_key
