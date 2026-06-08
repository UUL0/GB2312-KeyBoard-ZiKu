import sys
import os

def HanOut(infile,outfile):
    strA = ""
    OUTstr = ""
    idx = 256          # 当前字索引起始
    lst = []  # 用列表代替字符串
    lstC = [] # 字编存
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
            lst.append(strA + ":" + str(idx) + ":" + str(len(strA1)) +":" + strA1+ '\n')  # 写原数据+段、长


            for ch in strA1:
                lstC.append(f"{ch}:{idx}" + "\n") # 逐字格式化编号
                idx += 1

        # 一次性拼接（只创建1个新字符串）
        OUTstr = "".join(lst)
        # 输出结果到屏幕
        with open(outfile, 'w', encoding='utf-8') as f:
            f.write(OUTstr)
        print("范围段输出文件",outfile)

        respath=os.path.splitext(outfile)[0]  # 去掉后缀，保留路径
        with open(respath+"_字编.txt", 'w', encoding='utf-8') as f:
            f.write("".join(lstC))
        print("字编输出到文件",respath+"_字编.txt")
 

def main():
    # 1、取gia中protobuf hex
    if len(sys.argv) != 3:
        print("用法: python script.py <输入文件> <输出文件>")
        print("示例: python script.py input.txt output.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    HanOut(input_file,output_file)


# 程序入口
if __name__ == "__main__":
    main()