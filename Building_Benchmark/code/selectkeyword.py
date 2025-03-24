import json

# 输入 JSON 文件路径
input_file = "numina1_new.json"  # 请替换为实际文件路径
output_file = "numina1_new_nt_factor.json"

# 关键词
keywords = ["prime", "factor", "greatest common divisors", "least common multiples", "LCM", "GCD"]

# 读取 JSON 文件
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# 过滤包含 "Evaluate" 关键词的题目
filtered_data = [item for item in data if any(keyword in item["problem"] for keyword in keywords)]

# 保存筛选后的数据
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(filtered_data, f, indent=4, ensure_ascii=False)

print(f"筛选完成，共找到 {len(filtered_data)} 道题目，结果已保存到 {output_file}")

