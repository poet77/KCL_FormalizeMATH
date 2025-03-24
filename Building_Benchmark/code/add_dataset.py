import json
import os

def add_dataset_field(input_file, output_file):
    """给单个 JSON 文件中的每个数据项添加 dataset 字段"""
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        item['dataset'] = "MiniF2F"

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def process_folder(input_folder, output_folder):
    """批量处理指定文件夹下的所有 JSON 文件"""
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename)

            add_dataset_field(input_file, output_file)
            print(f"已处理文件: {filename}")

# 使用方法
input_folder = "Processing_new"   # 修改为你的输入文件夹路径
output_folder = "Processing_final" # 修改为你的输出文件夹路径
process_folder(input_folder, output_folder)