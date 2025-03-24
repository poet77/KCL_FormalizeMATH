import json
import re
import os

# 定义每个模板的关键词列表
templates = {
    "Probability": [r"probability"],
    "Sequence": [r"sequence"],
    "Set": [r"set", r"pair"],
    "Polynomial": [r"polynomial", r"expression"],
    "Function": [r"function", r"range"],
    "Equation": [r"solve", r"equation"],
    "Prime": [r"prime", r"factor", r"GCD", r"LCM"],
    "Digit": [r"digit", r"base", r"round"],
    "Number": [r"real number", r"integer", r"fraction"],
    "Combination": [r"permutation", r"How many ways", r"In how many orders"],
    # 可以继续添加其他模板
}

# 为每个模板创建正则表达式（不区分大小写）
patterns = {label: re.compile("|".join(keywords), re.IGNORECASE) for label, keywords in templates.items()}

def add_label(entry):
    problem_text = entry.get("informal_statement", "")
    
    for label, pattern in patterns.items():
        if pattern.search(problem_text):
            if "label" in entry:
                if isinstance(entry["label"], list):
                    if label not in entry["label"]:
                        entry["label"].append(label)
                else:
                    entry["label"] = [entry["label"], label]
            else:
                entry["label"] = [label]
    
    return entry

def process_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    new_data = [add_label(item) for item in data]

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=2, ensure_ascii=False)

def process_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.json'):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            
            process_json(input_path, output_path)
            print(f"{file_name} 已处理完成，结果保存在 {output_path}")

def main():
    input_folder = "Processing"  # 你的输入文件夹路径
    output_folder = "Processing_new"  # 你的输出文件夹路径
    process_folder(input_folder, output_folder)

if __name__ == "__main__":
    main()