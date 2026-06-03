aa20={'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'}

aa_order = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

seq_result = {}
read_file_name = "Lab3/data/seqs_fasta.txt"
write_file_name = "Lab3/data/result_5.txt"

# 初始化总计数
all_aa_count = {aa: 0 for aa in aa_order}
total_all = 0

current_id = None
current_seq = ""

# 读取FASTA文件
with open(read_file_name, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        # 处理序列ID行
        if line.startswith(">"):
            if current_id and current_seq:
                seq_len = len(current_seq)
                # 统计每个氨基酸的数量
                aa_count = {aa: current_seq.count(aa) for aa in aa_order}
                # 计算频率，保留1位小数
                freq = {aa: round((cnt / seq_len) * 100, 1) for aa, cnt in aa_count.items()}
                seq_result[current_id] = freq
                # 累加总计数
                for aa in aa_order:
                    all_aa_count[aa] += aa_count[aa]
                total_all += seq_len
            # 重置当前序列
            current_id = line[1:]
            current_seq = ""
        else:
            # 拼接序列，统一大写
            current_seq += line.upper()

# 处理最后一条序列
if current_id and current_seq:
    seq_len = len(current_seq)
    aa_count = {aa: current_seq.count(aa) for aa in aa_order}
    freq = {aa: round((cnt / seq_len) * 100, 1) for aa, cnt in aa_count.items()}
    seq_result[current_id] = freq
    for aa in aa_order:
        all_aa_count[aa] += aa_count[aa]
    total_all += seq_len

# 计算全体序列的频率
all_freq = {aa: round((all_aa_count[aa] / total_all) * 100, 1) if total_all > 0 else 0.0 for aa in aa_order}
seq_result["ALL"] = all_freq

with open(write_file_name, "w", encoding="utf-8") as f:
    # 写入表头
    header = f"{'ID':<6}" + "".join([f"{aa:>5} " for aa in aa_order]) + "\n"
    f.write(header)
    
    # 遍历每条序列，固定列宽6字符，右对齐
    for seq_id, freq in seq_result.items():
        # 按表头顺序生成数据行，每个数字占6字符，右对齐，保留1位小数
        row = [f"{freq[aa]:>6.1f}" for aa in aa_order]
        # ID占6字符左对齐，拼接数据行
        line_out = f"{seq_id:<6}" + "".join(row) + "\n"
        f.write(line_out)
