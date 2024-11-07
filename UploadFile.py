# import requests
from _sys import logger

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

def main(urls, token):
    # logger.info(urls)
    attachments = []
    
    for i in range(len(urls)):
        try:
            # 下载文件
            logger.info(urls)
            response = requests.get(urls[i]["fileURL"], stream=True)
            response.raise_for_status()
            imageBuffer = response.content
            bufferSize = len(imageBuffer)

            # 创建表单数据
            formData = MultipartEncoder(
                fields={
                    'parent_type': 'bitable_image',  # 如果上传到其他文档中，请修改这里
                    'size': str(bufferSize),
                    'file': (urls[i]["fileKey"] + '.jpg', imageBuffer, 'image/jpg')
                }
            )

            # 设置请求头
            logger.info(formData.content_type)
            logger.info(urls[i]['type'])
            headers = {
                'X-PLUGIN-TOKEN': token,
                'X-USER-KEY': '7365516029109256195',
                'Content-Type': formData.content_type
            }
            
            # 上传文件
            upload_response = requests.post(
                'https://project.feishu.cn/open_api/lichenglingdemo/file/upload',
                headers=headers,
                data=formData
            )
            
            # 检查请求是否成功
            upload_response.raise_for_status()  

            # 获取文件token
            logger.info(upload_response.json())
            logger.info("-----------------")

            # 构造返回结果
            resp_data = upload_response.json()
            file = resp_data["data"][0]
            logger.info(resp_data)
            attachments.append(file)

        except requests.exceptions.RequestException as e:
            if e.response:
                # 打印出服务器响应的详细信息
                logger.info(e.response.json())
                logger.info(e.response.status_code)
                logger.info(e.response.headers)
            else:
                # 打印请求详细信息或设置请求时发生的错误
                logger.error(f"Request Error: {e}")
    ## for循环结束

    ## 返回结果
    return attachments




