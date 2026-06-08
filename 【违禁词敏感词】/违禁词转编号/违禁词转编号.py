import sys
import argparse

def convert_encoding(code_file, input_file, output_file):
    # 1. 读取编码文件，建立字符->数值的映射
    char_to_code = {}
    with open(code_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if ':' in line:
                char, code = line.split(':', 1)
                char_to_code[char] = code
    
    print(f"已加载 {len(char_to_code)} 个字符映射")
    
    # 2. 读取输入文件，逐行转换并写入输出
    with open(input_file, 'r', encoding='utf-8') as f_in, \
         open(output_file, 'w', encoding='utf-8') as f_out:
        
        for line in f_in:
            line = line.strip()
            if not line:
                f_out.write('\n')
                continue
            
            codes = []
            for char in line:
                if char in char_to_code:
                    codes.append(char_to_code[char])
                else:
                    codes.append('?')  # 未找到的字符标记为?
            
            f_out.write(':'.join(codes) + '\n')
    
    print(f"转换完成，结果已写入 {output_file}")

# 使用示例
# convert_encoding('编码文件.txt', '输入词.txt', '输出结果.txt')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='按编码表转换文本为数值序列')
    parser.add_argument('code_file', help='编码文件路径（每行格式：字符:数值）')
    parser.add_argument('input_file', help='输入文本文件路径（每行一个词/句子）')
    parser.add_argument('output_file', help='输出结果文件路径')
    
    args = parser.parse_args()
    convert_encoding(args.code_file, args.input_file, args.output_file)
