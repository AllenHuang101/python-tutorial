import requests
import uuid
import os

def download_image(url):
    print("開始下載：", url)
    # 發送網路請求，下載圖片
    response = requests.get(url, timeout=60)
    print("下載完成")

    # 圖片儲存並取名，使用 GUID + URL 副檔名
    url_path = url.split('?')[0]  # 移除查詢參數
    _, ext = os.path.splitext(url_path)
    if not ext:
        ext = '.jpg'  # 預設副檔名
    file_name = str(uuid.uuid4()) + ext

    with open(file_name, mode='wb') as file_object:
        file_object.write(response.content)

if __name__ == '__main__':
    url_list = [
        'https://www.han-lin.tw/wp-content/uploads/2019/08/%E7%B6%B2%E8%B7%AF%E8%B3%87%E8%A8%8A%E5%95%8F%E9%A1%8C-696x479.jpg',
        'https://www.children.org.tw/uploads/%E8%B7%A8%E5%9F%9F%E5%85%B1%E5%A5%BD/%E5%AE%98%E7%B6%B2%E5%9C%96_01-%E6%95%B8%E4%BD%8D%E6%95%99%E9%A4%8A%E4%B8%BB%E9%A1%8C_(1).png',
        'https://en.pimg.jp/115/474/654/1/115474654.jpg'
    ]

    for item in url_list:
        download_image(item)
