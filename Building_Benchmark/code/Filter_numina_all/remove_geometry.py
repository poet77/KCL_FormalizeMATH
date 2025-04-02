import json

# 定义平面几何相关关键词
geometry_keywords = ['circle', 'line', 'graph', 'triangle', 'polygon', 'rectangle', 'point', 'plane']

def filter_geometry_problems(input_json_file, output_json_file, deleted_json_file):
    # 读取输入JSON文件
    with open(input_json_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
    
    # 用于存储保留的题目和删除的题目
    kept_problems = []
    deleted_problems = []
    
    # 遍历问题，检查是否包含几何相关的关键词
    for problem in data:
        problem_text = problem.get("problem", "").lower()  # 获取problem并转为小写字母以便匹配
        if any(keyword in problem_text for keyword in geometry_keywords):
            deleted_problems.append(problem)  # 如果包含几何关键词，保存到删除列表
        else:
            kept_problems.append(problem)  # 如果不包含几何关键词，保留
    
    # 保存处理后的JSON文件
    with open(output_json_file, 'w', encoding='utf-8') as outfile:
        json.dump(kept_problems, outfile, ensure_ascii=False, indent=4)
    
    # 保存删除的几何部分JSON文件
    with open(deleted_json_file, 'w', encoding='utf-8') as deleted_file:
        json.dump(deleted_problems, deleted_file, ensure_ascii=False, indent=4)
    
    # 返回删除的数量
    return len(deleted_problems)

# 示例使用
# 设置文件路径
input_file = 'NuminaAll.json'  # 输入文件路径
output_file = 'final_combined_data3.json'  # 输出文件路径
deleted_json_file = 'deleted_geometry.json'  # 删除的几何部分题目保存路径

# 执行函数并返回删除的数量
deleted_count = filter_geometry_problems(input_file, output_file, deleted_json_file)
print(f"删除的几何部分题目数量: {deleted_count}")
