import json


def filter_keys(obj, prefix):
    result = {}
    for key, value in obj.items():
        if isinstance(value, dict):
            # Nếu giá trị là một đối tượng dict, gọi đệ quy để lọc các khóa bên trong
            filtered_subkeys = filter_keys(value, prefix)
            if filtered_subkeys:
                result[key] = filtered_subkeys
        elif isinstance(key, str) and key.startswith(prefix):
            # Nếu khóa bắt đầu bằng "ABC", thêm vào kết quả
            result[key] = value
    return result




def process_json(input_file_path, output_file_path, prefix):
    with open(input_file_path, 'r',encoding= 'utf-8') as file:
        data = json.load(file)
        combina = data["data"]
        #print(combina)
        list_url = {}
        count = 0
        for i in combina:
            key_of_data = combina[i]
            for sub_combine in key_of_data["combinations"]:
                #print()
                count = count+1
                url = sub_combine["gStaticUrl"]
                key = url.split("/")[-1].split(".")[0]
                print(key)
                list_url[key] = url

        print(count)
        print(list_url)
        # filtered_values = [value for key, value in data.items() if key.startswith(prefix)]
        # print(filtered_values)
        with open(output_file_path, 'w',encoding="utf-8") as output_file:
            json.dump(list_url, output_file, indent=2)

# Thay thế các đối số sau đây bằng thông tin tệp JSON thực tế của bạn
input_file_path = 'E:\EmojiResource\metadata.json'
output_file_path = 'E:\EmojiResource\output_file.json'
prefix_to_filter = 'gStaticUrl'

process_json(input_file_path, output_file_path, prefix_to_filter)