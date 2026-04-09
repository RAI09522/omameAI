import 

# 1 ファイルから知識を読み取る関数
def load_brain(file_path):
    brain_data = {}
    if os.path.exists(file_path):
        with open(file_path, "r", ecoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if "|" in line:
                    key, val = line.split("|", 1)
                    brain_data[key] = val
    return brain_data 
# 2 新しい知識をファイルに書き込む関数
def save_knowledge(file_path, key, val):
    with open (file_path, "a", ecoding="utf-8") as f: #"a"は追記用
