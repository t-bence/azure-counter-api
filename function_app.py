import azure.functions as func
import logging
from lib.functions import read_count, increment_count, write_count

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="count_visitors")
def count_visitors(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Define the file path
    file_path = 'visitors.json'

    try:
        count = read_count(file_path)
        new_count = increment_count(count)
        write_count(file_path, new_count)
    except:
        return func.HttpResponse(-1, status_code=400)
    return func.HttpResponse(count, status_code=200)