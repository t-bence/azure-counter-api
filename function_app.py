import json
import os

import azure.functions as func
import logging

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

def write_count(file_path: str, count: int) -> None:

    data = dict(visitors=count)

    # Write the updated data back to the JSON file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="count_visitors")
def count_visitors(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Define the file path
    file_path = 'visitors.json'

    try:
        count = read_count(file_path)
        write_count(file_path, count + 1)
    except:
        return func.HttpResponse(-1, status_code=400)
    return func.HttpResponse(count, status_code=200)