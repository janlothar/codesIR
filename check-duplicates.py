import json
import sys
import os

def check_for_duplicates(input_path):
    with open(input_path, 'r') as f:
        data = json.load(f)

    aircon = data.get("aircon", {})
    ir_to_keys = {}
    duplicates = {}

    for key, ir in aircon.items():
        if ir in ir_to_keys:
            duplicates.setdefault(ir, []).append(key)
        else:
            ir_to_keys[ir] = key

    if duplicates:
        print("Duplicate IR codes found:")
        for ir, keys in duplicates.items():
            print(f"IR code: {ir}")
            print("  Used in keys:", [ir_to_keys[ir]] + keys)
    else:
        print("No duplicate IR codes found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {os.path.basename(__file__)} <input_file.json>")
        sys.exit(1)

    check_for_duplicates(sys.argv[1])