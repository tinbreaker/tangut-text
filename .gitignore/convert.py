import pandas as pd

# 读取CSV文件，将character列明确指定为字符串类型
df = pd.read_csv('类林_lèi lín.csv', dtype={'character': str}, na_filter=False)

# 创建输出字符串
output = ""
current_line = ""

# 遍历每一行数据
for index, row in df.iterrows():
    # 获取当前字符和character number，确保字符是字符串类型
    char = str(row['character']).strip()  # 去除前后空格
    char = '@' if not char or char.isspace() else char  # 如果是空或空格，替换为@
    char_num = row['character number']
    
    # 如果character number是1且不是第一个字符，先添加换行
    if char_num == 1 and current_line:
        output += current_line + "\n"
        current_line = char
    else:
        current_line += char

# 添加最后一行
if current_line:
    output += current_line

# 将结果写入markdown文件
with open('output.md', 'w', encoding='utf-8') as f:
    f.write(output)

# 打印结果预览
print("转换结果：")
print(output)
