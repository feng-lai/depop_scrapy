import os
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from bs4 import BeautifulSoup

# 输入的产品页面URL
product_page_url = "https://www.depop.com/products/vintage_pie_-dent-wizard-embroidered-cap-vintage/?moduleOrigin=meganav"

# 初始化WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(product_page_url)

# 使用WebDriverWait等待元素加载
wait = WebDriverWait(driver, 10)

# 提取标题
try:
    title_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.sc-grYavY.ProductDetailsSticky-styles__ProductTitle-sc-acdd0d1d-1.HXICV.eDSotq")))
    title = title_element.text.strip()
    print(f"提取到标题: {title}")
except TimeoutException:
    title = "Title not found"
    print("未能提取到标题")

# 提取价格
try:
    price_element = wait.until(EC.presence_of_element_located((By.XPATH, "//p[@aria-label='Price' and @class='sc-eDnWTT Price-styles__FullPrice-sc-f7c1dfcc-0 kcKICQ hmFDou']")))
    price = price_element.text.strip().replace("$", "")
    print(f"提取到价格: {price}")
except NoSuchElementException:
    price = "Price not found"
    print("未能提取到价格")

# 提取描述
description = ""
try:
    description_div = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.sc-eDnWTT.styles__TextContainer-sc-d367c36f-1.kcKICQ.cMiMZK")))
    soup = BeautifulSoup(description_div.get_attribute('innerHTML'), 'html.parser')
    description = soup.get_text(strip=True)
    print("提取到描述文本")
except NoSuchElementException:
    description = "Description not found"
    print("未能提取到描述")

# 提取图片
images = []
try:
    image_containers = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cSDegn")))
    for container in image_containers:
        img_element = container.find_element(By.TAG_NAME, "img")
        img_src = img_element.get_attribute('src')
        match = re.search(r'/(\d+)_(\w+)/P(\d+)\.jpg', img_src)
        if match:
            img_id = match.group(1)
            hash_value = match.group(2)
            img_name = f"{img_id}_{hash_value}P{match.group(3)}.jpg"
            images.append(img_name)
        else:
            images.append(img_src)
    print(f"提取到图片名称: {images}")
except TimeoutException:
    print("未能提取到图片")
    images = ["No images found"] * 8

# 提取选项信息
options = []
try:
    option_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "hhZyAr")))
    option_elements = option_container.find_elements(By.CLASS_NAME, "dqzKmZ")
    for option in option_elements:
        option_name = option.find_element(By.TAG_NAME, "span").text.strip()
        options.append(option_name)
    print(f"提取到选项信息: {options}")
except TimeoutException:
    print("未能提取到选项信息")
    options = ["No options found"]

# 提取评价信息
reviews = []
try:
    review_list = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "iqBfak")))
    review_items = review_list.find_elements(By.TAG_NAME, "li")
    for item in review_items:
        author = item.find_element(By.CLASS_NAME, "hyRbZr").text.strip()
        content = item.find_element(By.CLASS_NAME, "kMsyxA").text.strip()
        reviews.append({"name": author, "content": content, "level": 5})  # 假设所有评价等级为5
    print(f"提取到评价信息: {reviews}")
except TimeoutException:
    print("未能提取到评价信息")
    reviews = [{"name": "No author", "content": "No content", "level": 5}]

# 构建产品信息字典
product_info = {
    'price': price,
    'itm_name': title,
    'img1': images[0] if len(images) > 0 else "",
    'img2': images[1] if len(images) > 1 else "",
    'img3': images[2] if len(images) > 2 else "",
    'img4': images[3] if len(images) > 3 else "",
    'img5': images[4] if len(images) > 4 else "",
    'img6': images[5] if len(images) > 5 else "",
    'img7': images[6] if len(images) > 6 else "",
    'img8': images[7] if len(images) > 7 else "",
    'itm_dsc': description,
    'cat_id': "57",  # 根据实际情况填写
    's_id': "307",  # 根据实际情况填写
    'attr': options,
    'eva': reviews
}

# 读取上传结果文件
upload_results_path = 'upload_results.json'
with open(upload_results_path, 'r', encoding='utf-8') as f:
    upload_results = json.load(f)

# 替换图片字段
for i in range(len(images)):
    key = f'img{i+1}'
    if key in product_info and product_info[key] in [result['original_img'] for result in upload_results]:
        original_img = product_info[key]
        for result in upload_results:
            if result['original_img'] == original_img:
                product_info[key] = result['new_img']
                break

# 将数据转换为JSON格式并保存到当前目录
json_file_path = 'product_info.json'
with open(json_file_path, 'w', encoding='utf-8') as f:
    json.dump(product_info, f, ensure_ascii=False, indent=4)

print(f"替换图片后的完整JSON已保存到 '{json_file_path}'")

# 关闭WebDriver
driver.quit()