import sys

def FstrOut(infile,outfile):
    SAstr = r""" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=[]\;',./~!@#$%^&*()_+{}|:"<>?·【】、；’，。！￥…（）—：”《》？√Σ∏∫±≈≠≥≤⊥∝∈∉⊃⊂∪∩∅ℕℤℚℝℂ∨↔→∀∃∴∵⊕⊢⊤πφγ∞ΔΩΘθλζεβαημρστψωικ∠⊿∟≌§％℉℃℅‰￡※＄￠∮•¤≮≯"""

    SBstr = r"""√Σ∏∫±≈≠≥≤⊥∝∈∉⊃⊂∪∩∅ℕℤℚℝℂ∨↔→∀∃∴∵⊕⊢⊤⊥πφγ∞ΔΩΘθλζεβαημρστψωικ∠⊿∟≌§％℉℃℅‰￡※￥＄￠∮•¤≮≯"""
    def show(ch):
        if ch == '\n':
            return '\\n'
        elif ch == '\r':
            return '\\r'
        elif ch == '\t':
            return '\\t'
        else:
            return ch
    with open(outfile, 'w', encoding='utf-8') as f:
        for ch in SBstr:
            pos = SAstr.find(ch) + 1
            f.write(f"{show(ch)}索引位：{pos}\n")  # 写入文件

def main():
    # 1、取gia中protobuf hex
    if len(sys.argv) != 3:
        print("用法: python script.py <输入文件> <输出文件>")
        print("示例: python script.py input.txt output.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    FstrOut(input_file,output_file)


# 程序入口
if __name__ == "__main__":
    main()