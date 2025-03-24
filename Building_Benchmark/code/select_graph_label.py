import json
import re

# 定义需要匹配的关键词列表
keywords = [
    r"\nA:", r"below", r"graph", r"\nA"
]

pattern = re.compile("|".join(keywords))

def add_label(entry):
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

# 处理 JSON 文件
def process_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    new_data = [add_label(item) for item in data]

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=2, ensure_ascii=False)

# 用法示例
process_json("numina01_noc_nog.json", "output_labeled.json")