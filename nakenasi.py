import os
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