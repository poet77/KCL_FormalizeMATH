import os
import json

# 定义文件夹路径
base_dir = 'E:/KCL_Lab/KCL_FormalizeMATH/Building_Benchmark/numina_all'

# 需要提取的 JSON 文件列表
json_files = [
    'combination.json',
    'digit.json',
    'equation.json',
    'function.json',
    'number.json',
    'polynomial.json',
    'prime.json',
    'probability.json',
    'sequence.json',
    'set.json'
]

# 用于存储所有文件内容的合并数据
final_data = []

# 遍历 numina_all 文件夹下的 numina01, numina02, ..., numina05 子文件夹
for i in range(1, 6):
    folder_name = f'numina{i:02d}'  # 格式化文件夹名为 numina01, numina02 等
    folder_path = os.path.join(base_dir, folder_name)

    # 存储当前文件夹的所有 JSON 数据
    folder_data = {}

    # 遍历每个文件名并读取数据
    for json_file in json_files:
        combination_file = os.path.join(folder_path, json_file)

        # 确保文件存在并且是有效的 JSON 文件
        if os.path.exists(combination_file):
            with open(combination_file, 'r', encoding='utf-8') as f:
                try:
                    dataset = json.load(f)  # 读取 JSON 内容
                    i = 0
                    # 处理每个 JSON 文件，统一格式
                    for data in dataset:
                        label = os.path.splitext(json_file)[0]  # 去除 '.json' 后缀
                        entry = {
                            "source": data.get("source", ""),  # 假设所有数据的 source 相同
                            "problem": data.get("problem", ""),
                            "solution": data.get("solution", ""),
                            "dataset": "Numina",  # 假设数据集是固定的
                            "label": [label]  # 使用文件夹名作为 label
                        }
                        final_data.append(entry)

                    # 其他文件（digit, equation等）可以根据需要额外处理
                    # 例如，我们可以将这些数据合并到 final_data 中的某些字段（根据需求）

                except json.JSONDecodeError:
                    print(f"Error decoding JSON in {combination_file}")
        else:
            print(f"{combination_file} does not exist.")

# 将合并后的数据写入一个新的 JSON 文件
output_file = 'final_combined_data.json'
with open(output_file, 'w', encoding='utf-8') as outfile:
    json.dump(final_data, outfile, indent=4, ensure_ascii=False)

print(f"Final combined data has been saved to {output_file}")
