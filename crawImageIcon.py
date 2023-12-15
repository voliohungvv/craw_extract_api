import os
from concurrent.futures import ThreadPoolExecutor

import requests


def download_and_save(url, save_directory):
    response = requests.get(url)

    if response.status_code == 200:
        # Lấy tên tệp từ URL
        file_name = url.split("/")[-1]

        # Xác định đường dẫn lưu trữ tệp
        save_path = os.path.join(save_directory, file_name)

        # Ghi nội dung tải về vào tệp
        with open(save_path, 'wb') as file:
            file.write(response.content)

        print(f"Đã tải xuống và lưu trữ tại: {save_path}")
    else:
        print(f"Lỗi {response.status_code} khi tải xuống từ {url}")


def read_and_download_from_file(file_path, save_directory):
    with open(file_path, 'r') as file:
        # Đọc từng dòng trong tệp văn bản
        for line in file:
            # Loại bỏ khoảng trắng và ký tự xuống dòng từ mỗi dòng
            url = line.strip()

            # Kiểm tra xem dòng có chứa URL hợp lệ hay không
            if url:
                # Tải xuống và lưu trữ từng URL
                download_and_save(url, save_directory)

def read_and_download_from_file2(file_path, save_directory):
    with open(file_path, 'r') as file:
        # Đọc từng dòng trong tệp văn bản
        urls = [line.strip() for line in file if line.strip()]

    # Tạo thư mục nếu nó không tồn tại
    os.makedirs(save_directory, exist_ok=True)

    # Sử dụng ThreadPoolExecutor để tải xuống đồng thời
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Chạy download_and_save cho mỗi URL
        executor.map(lambda url: download_and_save(url, save_directory), urls)

# Đường dẫn của tệp chứa danh sách các URL
file_path = 'E:\EmojiResource/url_mix_result.txt'

# Thư mục để lưu trữ tệp tải xuống
download_directory = 'E:\EmojiDownloaded'

# Tạo thư mục nếu nó không tồn tại
os.makedirs(download_directory, exist_ok=True)

# Đọc từng dòng từ tệp và tải xuống
read_and_download_from_file2(file_path, download_directory)
