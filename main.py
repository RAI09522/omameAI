import os

# 1 ファイルから知識を読み取る関数
def load_brain(file_path):
    brain_data = {}
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if "|" in line:
                    key, val = line.split("|", 1)
                    brain_data[key] = val
    return brain_data 

# 2 新しい知識をファイルに書き込む関数
def save_knowledge(file_path, key, val):
    with open(file_path, "a", encoding="utf-8") as f: # "a"は追記用
        f.write(f"{key}|{val}\n")
    print(f"「{key}」について新しく覚えました！")

# --- 変更点：プログラムと同じフォルダーの「brain.txt」の絶対パスを自動計算 ---
# __file__ はこのプログラムファイル自身の場所を表します
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "brain.txt")

# メイン処理
print("学習型検索システム（自動保存モード）")
print(f"保存先: {file_path}") # どこに保存されるか画面に表示します

while True:
    brain = load_brain(file_path) # 常に最新の知識を読み込む

    print("\n[1] 話す [2] 学習させる [exit] 終了")
    mode = input("モードを選択:")

    if mode == "1":
        user_input = input("なんだよぉ:")
        found = False
        # 登録されているキーワードを1つずつチェック
        for key in brain:
            if key in user_input: # ユーザーの入力にキーワードが含まれていたら
                print(f"大豆: {brain[key]}")
                found = True
                break # 1つ見つかったら検索を終了
                
        if not found:
            print("大豆: なんだそれ[2]で教えてくれよ")
            
    elif mode == "2":   
        new_key = input("何を覚える？(例：みかん) : ")
        new_val = input("その回答は？(例 : オレンジ色の果物だよ) : ") 
        save_knowledge(file_path, new_key, new_val)
    
    elif mode == "exit":
        print("システムを終了します。")
        break
