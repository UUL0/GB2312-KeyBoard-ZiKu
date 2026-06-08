import sys
import os

def HanYinOut(infile,outfile):
    strA = ""
    strA1 = ""
    OstrA = ""
    OUTstr = ""
    lst = []  # 用列表代替字符串
    # 读取文件

    with open(infile, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()  # 去除首尾空白字符
        
            # 跳过空行和没有冒号的行
            if not line or ':' not in line:
                continue
        
            # 分割冒号前后的内容（只分割第一个冒号）
            strA, strA1 = line.split(':', 1) # 分割第一个冒号两边数据
            strA = strA.strip()
            strA1 = strA1.strip() # 首尾空白去除，文字数据
            OUTstr = strA + ":" + strA1+ '\n'

            PDec = 0 # 32bit有符号整数，作为拼音编码
            for ch in strA:  
                num = ord(ch) - ord('a') + 1  # a=1, b=2, ..., z=26  用ord当前字符的Ascii-字符a的位置得到0~N
                PDec = (PDec << 5) | num # 以0~29bit对应最多6个字母，先左移5bit后或运算，无需解码，拼音按顺序输入时也是这样，通过输入的值比对索引到拼音位置
            lst.append(str(PDec) + ":" + OUTstr)  # 写原数据，并在前面追加32位整数（5bit代表一个字母）

        # 一次性拼接（只创建1个新字符串）
        OUTstr = "".join(lst)
        # 输出结果到屏幕
        with open(outfile, 'w', encoding='utf-8') as f:
            f.write(OUTstr)
        print("拼音编码输出文件",outfile)
 

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