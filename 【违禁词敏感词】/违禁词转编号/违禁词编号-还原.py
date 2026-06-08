import sys
import argparse

def restore_text(code_file, input_file, output_file):
    # 1. 加载编码表
    char_map = {}
    with open(code_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or ':' not in line:
                continue
            parts = line.split(':', 1)
            if len(parts) != 2:
                continue
            char, code = parts
            if not char:
                continue
            try:
                char_map[int(code)] = char
            except ValueError:
                continue

    print(f"✅ 已加载 {len(char_map)} 个字符映射")

    # 2. 读取输入文件（按行处理）
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 3. 还原（关键：按行分割，不要全局 split）
    result = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # 按冒号分割这一行的所有数字
        for num_str in line.split(':'):
            num_str = num_str.strip()
            if num_str:
                try:
                    num = int(num_str)
                    if num in char_map:
                        result.append(char_map[num])
                    else:
                        result.append(f'[?{num}]')
                except ValueError:
                    result.append(f'[ERR:{num_str}]')
        
        result.append('\n')  # 保留换行

    restored = ''.join(result).rstrip()  # 去掉最后多余的换行

    # 4. 输出
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(restored)
        print(f"✅ 已保存到 {output_file}")
    else:
        print(f"📝 还原结果:\n{restored}")

    return restored


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='数字编码还原为文字')
    parser.add_argument('code_file', help='编码文件')
    parser.add_argument('input_file', help='输入文件（数字序列）')
    parser.add_argument('-o', '--output', help='输出文件')
    
    args = parser.parse_args()
    restore_text(args.code_file, args.input_file, args.output)
