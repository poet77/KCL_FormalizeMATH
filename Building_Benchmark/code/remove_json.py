import json
import os

# 读取 JSON 数据文件
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# 保存修改后的数据到新文件
def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# 删除包含 "label": ["delete"] 的元素
def remove_delete_labels(data):
    return [item for item in data if item.get("label") != ["delete"]]

def process_folder(input_folder, output_folder):
    # 如果输出文件夹不存在则创建
    os.makedirs(output_folder, exist_ok=True)
    
    # 遍历输入文件夹下所有 JSON 文件
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.json'):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            
            data = load_json(input_path)
            filtered_data = remove_delete_labels(data)
            save_json(filtered_data, output_path)
            
            print(f"{file_name} 处理完成，已保存到 {output_path}")

def main():
    input_folder = 'json_ncg'   # 输入文件夹路径（自行替换）
    output_folder = 'json_remove' # 输出文件夹路径（自行替换）
    
    process_folder(input_folder, output_folder)

if __name__ == "__main__":
    main()