import json
from collections import Counter

# 定义 JSON 文件的路径
json_file = 'NuminaAll_2.json'  # 替换为你的 JSON 文件路径

# 用于存储所有 labels 的计数
label_counts = Counter()

# 打开并读取 JSON 文件
with open(json_file, 'r', encoding='utf-8') as f:
    try:
        # 读取 JSON 数据
        data = json.load(f)
        
        # 遍历每个条目，提取 'label'
        for entry in data:
            labels = entry.get('label', [])
            
            # 统计每个 label 的数量
            label_counts.update(labels)
            
    except json.JSONDecodeError:
        print(f"Error decoding JSON in {json_file}")

# 输出每个标签的数量
for label, count in label_counts.items():
    print(f"Label '{label}' appears {count} times.")
