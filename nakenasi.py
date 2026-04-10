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
        f.write(f"{key}|{val}\n")
    print(f"「{key}」について新しく覚えました！")
# メイン処理
print("学習型検索システム")
file_path = input("brain.txtをドロップしてEnterを押してください").strip().strip('"')

while True:
    brain = load_brain(file_path) # 常に最新の知識を読み込む

    print("\n[1] 検索する [2] 学習させる [exit] 終了")
    mode = input("モードを選択:")

    if mode == "1":
        user_input = input("何か話してください:")
        found = False
        for key in brain:
             print(f"AI: {brain[key]}")
             found = True
        if not found:
            print("AI: なんだそれ[2]で教えてくれよ")
    elif mode == "2":   
        
