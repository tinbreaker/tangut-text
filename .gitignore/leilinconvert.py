from pathlib import Path
import pandas as pd
import sys

def process_leilin_data(input_csv='类林_lèi lín.csv', output_md='类林_lèi lín.md'):
    try:
        # 获取路径
        root_dir = Path(__file__).parent.parent
        csv_path = root_dir / input_csv
        output_path = root_dir / output_md

        # 检查输入文件是否存在
        if not csv_path.exists():
            raise FileNotFoundError(f"找不到CSV文件: {csv_path}")

        # 读取CSV文件
        df = pd.read_csv(csv_path, dtype={'character': str}, na_filter=False)

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
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output)

        # 打印结果预览
        print("转换结果：")
        print(output)
        print(f"\n文件已保存至: {output_path}")

    except FileNotFoundError as e:
        print(f"错误: {e}")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"错误: CSV文件为空")
        sys.exit(1)
    except PermissionError:
        print(f"错误：没有写入权限 - {output_path}")
        sys.exit(1)
    except Exception as e:
        print(f"发生未知错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    process_leilin_data()