import json

# 假设 data 是一个包含字典的列表
with open('E:/AI4MATH_RESEARCH/Dataset/NuminaMath-CoT/Processing_new/MiniF2F_New.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 过滤掉 label 数组中有空字符串的项
cleaned_data = [
    item for item in data
    if all(label.strip() != "" for label in item.get('label', []))
]

# 保存结果
with open('E:/AI4MATH_RESEARCH/Dataset/NuminaMath-CoT/Processing_new/MiniF2F_New2.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_data, f, indent=2, ensure_ascii=False)
