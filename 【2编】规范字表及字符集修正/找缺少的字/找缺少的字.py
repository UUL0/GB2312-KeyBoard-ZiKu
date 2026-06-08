def find_missing(full_file, target_file, output_file):
    with open(full_file, 'r', encoding='utf-8') as f:
        full_chars = set(f.read())

    with open(target_file, 'r', encoding='utf-8') as f:
        target_chars = set(f.read())

    missing = full_chars - target_chars
    missing = {c for c in missing if not c.isspace()}

    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"缺少 {len(missing)} 个字符：\n\n")
        for c in sorted(missing):
            f.write(f"{c}\n")

    print(f"已写入 {output_file}")

# 使用

find_missing('GB2312编码1.txt', '处理的GB2312编码.txt', '缺少的字.txt')
