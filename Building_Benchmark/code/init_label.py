import json

# 加载JSON文件
with open('E:/AI4MATH_RESEARCH/Dataset/NuminaMath-CoT/dataset/MiniF2F/MiniF2F_All.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 为每个问题添加默认的空label
for item in data:
    item['label'] = ""

# 将更新后的数据写回到文件（可以替换原文件，也可以另存为新文件）
with open('E:/AI4MATH_RESEARCH/Dataset/NuminaMath-CoT/dataset/MiniF2F/MiniF2F_New.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("标签已添加并保存至MiniF2F_New.json")

