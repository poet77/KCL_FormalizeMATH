import json
import os

def extract_by_label(data, label):
    """从数据集中提取包含指定标签的项"""
    return [item for item in data if label in item.get("label", [])]

def save_json(data, output_file):
    """保存为 JSON 文件"""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def process_single_file(input_file, output_dir):
    """处理单个 JSON 文件"""
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    labels_order = [
        "Combination", "Probability", "Prime", "Digit", 
        "Sequence", "Set", "Polynomial", "Function", 
        "Equation", "Number"
    ]

    remaining_data = data.copy()

    file_prefix = os.path.splitext(os.path.basename(input_file))[0]
    file_output_dir = os.path.join(output_dir, file_prefix)
    os.makedirs(file_output_dir, exist_ok=True)

    for label in labels_order:
        extracted_items = extract_by_label(remaining_data, label)
        save_json(extracted_items, os.path.join(file_output_dir, f'{label.lower()}.json'))
        print(f"[{file_prefix}] 提取 {label} 项：{len(extracted_items)} 条")
        
        remaining_data = [item for item in remaining_data if label not in item.get("label", [])]

    save_json(remaining_data, os.path.join(file_output_dir, 'remaining.json'))
    print(f"[{file_prefix}] 剩余数据已保存至 remaining.json")

def filter_dataset(input_path, output_dir):
    """根据条件提取标签数据并保存，支持输入为单文件或文件夹"""
    os.makedirs(output_dir, exist_ok=True)

    if os.path.isfile(input_path):
        process_single_file(input_path, output_dir)
    elif os.path.isdir(input_path):
        json_files = [f for f in os.listdir(input_path) if f.endswith('.json')]
        for file_name in json_files:
            input_file = os.path.join(input_path, file_name)
            process_single_file(input_file, output_dir)
    else:
        print("输入路径无效：既不是文件也不是文件夹")

# ✅ 示例用法（直接调用）
if __name__ == '__main__':
    input_path = 'Processing_final'  # 可以是 json 文件或文件夹
    output_directory = 'MiniF2F_all'  # 输出目录
    filter_dataset(input_path, output_directory)