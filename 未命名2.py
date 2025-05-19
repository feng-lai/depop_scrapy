import requests
import json

url = 'https://img.maiiepay.com/fleamark/pro_save'
headers = {'Content-Type': 'application/json'}

# 读取JSON文件
with open('product_info.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print(data)
# 发送POST请求
response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print("数据上传成功:")
    print(response.json())
else:
    print("数据上传失败:")
    print(response.json())
    # 检查响应中的错误信息
    error_response = response.json()
    if 'error' in error_response:
        print(f"错误信息: {error_response['error']}")