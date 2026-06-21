import json
import os

# 1. Get the directory where THIS script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. List the files
files_to_merge = ['ecoA.json', 'ecoB.json', 'ecoC.json', 'ecoD.json', 'ecoE.json']
combined_data = []

for file_name in files_to_merge:
    # 3. Join the script directory with the filename to get the full path
    file_path = os.path.join(script_dir, file_name)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                combined_data.extend(data)
        print(f"Successfully loaded {file_name}")
    except FileNotFoundError:
        print(f"Error: Could not find {file_name} at {file_path}")

# 4. Save the final file in the same folder as the script
output_path = os.path.join(script_dir, 'final_eco.json')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(combined_data, f, indent=2)

print(f"\nMerge complete! Saved to: {output_path}")