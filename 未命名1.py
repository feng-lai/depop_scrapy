import os
import requests
import json

url = 'https://img.maiiepay.com/fleamark/upload'
headers = {}  # 不需要设置Content-Type，因为我们将使用multipart/form-data

# 用于存储上传结果的列表
upload_results = []

# 读取JSON文件
with open('images_data.json', 'r', encoding='utf-8') as f:
    data_list = json.load(f)

# 遍历数据并发送POST请求
for data_item in data_list:
    img_file_name = data_item['img']  # 直接获取img字段
    img_path = os.path.join(os.getcwd(), img_file_name)  # 获取文件完整路径
    
    if not os.path.exists(img_path):
        print(f"警告: 文件 {img_file_name} 不存在，跳过上传。")
        continue

    with open(img_path, 'rb') as file:
        files = {'file': (img_file_name, file)}  # 使用原始的文件名
        
        try:
            response = requests.post(url, files=files)
            
            if response.status_code == 200:
                result = response.json()
                print("数据上传成功:")
                print(result)
                
                # 记录原始img字段和返回的新img字段
                original_img = img_file_name
                new_img = result['data']['img']
                upload_results.append({'original_img': original_img, 'new_img': new_img})
                
                # 输出单个上传成功的记录
                print(f"原始图片名: {original_img}")
                print(f"新图片名: {new_img}")
            else:
                print("数据上传失败:")
                print(response.json())
                
                # 检查响应中的错误信息
                error_response = response.json()
                if 'error' in error_response:
                    print(f"错误信息: {error_response['error']}")
        except requests.exceptions.RequestException as e:
            print(f"请求错误: {e}")
        except Exception as e:
            print(f"发生错误: {e}")

# 将上传结果保存到当前目录下的JSON文件中
output_json_file_path = 'upload_results.json'
with open(output_json_file_path, 'w', encoding='utf-8') as f:
    json.dump(upload_results, f, ensure_ascii=False, indent=4)

print(f"上传结果已保存到 '{output_json_file_path}'")