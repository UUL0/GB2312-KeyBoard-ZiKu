import sys
import os

# 取N列字符串

def HanYinOut(infile,outfile):
    strA = r"""=""" # 以什么作为行列分割
    strN = 0 # 取第几个元素
    lst = []  # 用列表代替字符串
    # 读取文件

    with open(infile, 'r', encoding='utf-8') as f:
        for line in f:
            # line = line.strip()  # 去除首尾空白字符
        
            # 跳过空行和没有冒号的行
            if not line or strA not in line:
                lst.append("\n") #直接写空\换行
                # continue # 跳过这次循环
            else:
                lst.append(line.split(strA)[strN]) # 全部分割 取某个元素 取字符存入列表

            # strA, strA1 = line.split(':', 1) # 分割第一个冒号两边数据


        # 输出结果到文件
        with open(outfile, 'w', encoding='utf-8') as f:
            f.write("".join(lst)) # 一次性拼接（只创建1个新字符串）
        print("输出文件：",outfile)
 

def main():
    # 1、取gia中protobuf hex
    if len(sys.argv) != 3:
        print("用法: python script.py <输入文件> <输出文件>")
        print("示例: python script.py input.txt output.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    HanYinOut(input_file,output_file)


# 程序入口
if __name__ == "__main__":
    main()