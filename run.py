import pandas as pd

# Đọc file CSV
file_path = 'duong_dan_den_file.csv'  # Thay đổi đường dẫn đến file CSV của bạn
df = pd.read_csv(file_path)

# In ra tên các cột
print("Các cột trong file CSV:")
for column in df.columns:
    print(column)
