import os
import json

def read_count(file_path: str) -> int:
    # Check if the file exists
    if os.path.exists(file_path):
        # Attempt to read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
            if 'visitors' not in data or not isinstance(data['visitors'], int):
                raise ValueError("Invalid data format. Resetting visitors count.")
    else:
        raise IOError("File not found.")

    return data['visitors']

def increment_count(count: int) -> int:
    return count + 1

def write_count(file_path: str, count: int) -> None:

    data = dict(visitors=count)

    # Write the updated data back to the JSON file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)