import json

# 读取JSON文件
def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# 写入去重后的JSON文件
def write_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# 删除重复问题
def remove_duplicates(data):
    seen_problems = set()
    unique_data = []
    removed_count = 0

    for entry in data:
        problem = entry.get('problem')
        if problem not in seen_problems:
            unique_data.append(entry)
            seen_problems.add(problem)
        else:
            removed_count += 1

    return unique_data, removed_count

# 主函数
def main(input_file, output_file):
    # 读取原始数据
    data = read_json(input_file)
    
    # 删除重复问题
    unique_data, removed_count = remove_duplicates(data)
    
    # 写入无重复问题的数据
    write_json(unique_data, output_file)
    
    print(f"删除了 {removed_count} 条重复数据")
    return removed_count

# 设置文件路径
input_file = 'final_combined_data.json'  # 输入文件路径
output_file = 'final_combined_data2.json'  # 输出文件路径

# 执行主函数
removed_count = main(input_file, output_file)
