import sys

def main():
    Mstr=""
    Mstr = r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=[]\;',./Shift~!@#$%^&*()_+{}|:"<>?·1234567890-=【】、；’，。、Shift~！@#￥%……&*（）——+{}|：”《》？√ Σ∏∫ ±≈ ≠ ≥ ≤⊥∝∈ ∉ ⊃⊂∪∩ ∅ℕℤℚℝℂ ∨↔→∀∃ ∴∵ ⊕⊢⊤⊥πφγ∞ΔΩΘθλζ εβαημρστψωικ∠⊿∟≌§％℉℃℅‰￡※￥＄￠∮•¤≮≯"""
    Mstr = "".join(dict.fromkeys(Mstr)) 
    with open('output符号去重.txt', 'w', encoding='utf-8') as f:
        f.write(Mstr)


# 程序入口
if __name__ == "__main__":
    main()