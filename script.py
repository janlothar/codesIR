import json
import sys
import os

def transform_aircon_json(input_path, output_path):
    with open(input_path, 'r') as f:
        data = json.load(f)

    result = {"commands": {}}
    aircon = data.get("aircon", {})

    for key, ir_code in aircon.items():
        if key == "off":
            result["commands"]["off"] = ir_code
            continue

        try:
            mode_part, fan_part, temp_part = key.split("_")
            mode = mode_part
            fan_mode = fan_part.replace("fan", "")
            temperature = temp_part.replace("C", "")

            result["commands"].setdefault(mode, {}).setdefault(fan_mode, {})[temperature] = ir_code
        except ValueError:
            print(f"Skipping unrecognized key format: {key}")

    with open(output_path, 'w') as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {os.path.basename(__file__)} <input_file.json> <output_file.json>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    transform_aircon_json(input_file, output_file)