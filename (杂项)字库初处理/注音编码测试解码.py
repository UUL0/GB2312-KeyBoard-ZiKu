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

            PDec = int(strA) # 整数字符串转为数值
            Pstr = ""
            while PDec > 0: # 解完结束
                num = PDec & 0x1F # 取数值低5位
                ch = chr(num + ord('a') - 1) # a字符起始+字母编码，转为Ascii字符
                Pstr = ch + Pstr # 向前拼接
                PDec >>= 5 # 右移5bit，为下一次取值计算
            lst.append(Pstr + ":" + OUTstr)  # 写原数据，并在前面追加32位整数（5bit代表一个字母）

        # 一次性拼接（只创建1个新字符串）
        OUTstr = "".join(lst)
        # 输出结果到屏幕
        with open(outfile, 'w', encoding='utf-8') as f:
            f.write(OUTstr)
        print("拼音解码输出文件",outfile)
 

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