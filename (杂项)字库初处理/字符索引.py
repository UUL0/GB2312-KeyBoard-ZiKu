import sys
import os

def StrOut(infile,outfile):
    OstrA = r""" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=[]\;',./~!@#$%^&*()_+{}|:"<>?·【】、；’，。！￥…（）—：”《》？√Σ∏∫±≈≠≥≤⊥∝∈∉⊃⊂∪∩∅ℕℤℚℝℂ∨↔→∀∃∴∵⊕⊢⊤πφγ∞ΔΩΘθλζεβαημρστψωικ∠⊿∟≌§％℉℃℅‰￡※＄￠∮•¤≮≯"""
    idx = 1          # 当前字索引起始
    lstC = [] # 字编存
    for ch in OstrA:
        lstC.append(f"{ch}:{idx}" + "\n") # 逐字格式化编号
        idx += 1

    with open(outfile, 'w', encoding='utf-8') as f:
        f.write("".join(lstC))
    print("符号编输出到文件",outfile)
 

def main():
    # 1、取gia中protobuf hex
    if len(sys.argv) != 2:
        print("用法: python script.py <输出文件>")
        print("示例: python script.py output.txt")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[1]
    StrOut(input_file,output_file)


# 程序入口
if __name__ == "__main__":
    main()