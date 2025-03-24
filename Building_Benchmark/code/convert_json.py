import json
import os

def process_json(input_file, output_file):
    """处理单个 JSON 文件"""
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 将每个 json 字符串解析出来，取出 problem 和 solution
    result = []
    for line in lines:
        data = json.loads(line)
        result.append({
            "source": data.get("source", ""),
            "problem": data.get("problem", ""),
            "solution": data.get("solution", "")
        })

    # 输出为一个数组格式
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

def process_folder(input_folder, output_folder):
    """处理文件夹中的所有 JSON 文件"""
    # 如果输出文件夹不存在，则创建它
    os.makedirs(output_folder, exist_ok=True)

    # 遍历文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename)

            # 处理每个 JSON 文件
            process_json(input_file, output_file)
            print(f"已处理文件: {filename}")

# 用法示例：处理文件夹中的所有 JSON 文件
input_folder = "json"  # 你的输入文件夹路径
output_folder = "json_new"  # 你的输出文件夹路径
process_folder(input_folder, output_folder)