import sys

def KeyMOut(infile,outfile):
    OstrA = ""
    OUTstr = ""
    idx = 0          # 当前列表索引
    lst = []  # 用列表代替字符串
    Mstr = "" # 内容连接
    lst.append("")
    # 读取文件

    with open(infile, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()  # 去除首尾空白字符
        
            # 跳过空行和没有冒号的行
            if not line or ':' not in line:
                continue
        
            # 分割冒号前后的内容（只分割第一个冒号）
            strA, strA1 = line.split(':', 1)
            strA = strA.strip()
            strA1 = strA1.strip()
        
            # 判断是否与上一个记录相同
            if strA != OstrA:
                # 不同：追加换行 + 完整记录
                # lst.append('\n' + strA + ":" + strA1)  # 追加到列表
                Mstr = "".join(dict.fromkeys(Mstr)) 
                lst[idx] += Mstr  # 写上一次记录
                lst.append('\n' + strA + ":")  # 追加到列表
                Mstr = strA1
                OstrA = strA  # 更新上一个记录
                idx += 1
            else:
                # 相同：直接追加内容（不换行，不重复key）
                # lst[idx] += strA1
                Mstr  += strA1

        Mstr = "".join(dict.fromkeys(Mstr)) # 用字符串的每个字符当字典的key，key是唯一，所以结果是去重汉字
        lst[idx] += Mstr  # 写上一次记录
        # 一次性拼接（只创建1个新字符串）
        OUTstr = "".join(lst)
        # 输出结果到屏幕
        with open(outfile, 'w', encoding='utf-8') as f:
            f.write(OUTstr)
        print("输出到文件",{outfile})


def main():
    # 1、取gia中protobuf hex
    if len(sys.argv) != 3:
        print("用法: python script.py <输入文件> <输出文件>")
        print("示例: python script.py input.txt output.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    KeyMOut(input_file,output_file)


# 程序入口
if __name__ == "__main__":
    main()