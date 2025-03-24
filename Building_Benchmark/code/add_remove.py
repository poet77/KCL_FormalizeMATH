import json
import re
import os

# 定义需要匹配的关键词列表
keywords = [
    r"\(A\)", r"\nA;", r"\(1\)", r"\(I\)", r"\$\(\d+\)\$", r"A\)", r"below", r"graph", r"\nA", r"\nA:", r"decimal", r"domain"
]

pattern = re.compile("|".join(keywords))

def add_label(entry):
    """为包含特定关键词的条目添加 'delete' 标签"""
    problem_text = entry.get("problem", "")
    if pattern.search(problem_text):
        if "label" in entry:
            if isinstance(entry["label"], list):
                entry["label"].append("delete")
            else:
                entry["label"] = ["delete"]
        else:
            # 如果 'label' 字段不存在，则创建一个新的列表并添加 "delete"
            entry["label"] = ["delete"]
    return entry

def process_json(input_file, output_file):
    """处理单个 JSON 文件"""
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    new_data = [add_label(item) for item in data]

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=2, ensure_ascii=False)

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
input_folder = "E:/AI4MATH_RESEARCH/Dataset/NuminaMath-CoT/dataset/MiniF2F"  # 你的输入文件夹路径
output_folder = "E:/AI4MATH_RESEARCH/Dataset/NuminaMath-CoT/dataset/MiniF2F/New"  # 你的输出文件夹路径
process_folder(input_folder, output_folder)