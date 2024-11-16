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
        logging.info("Start reading")
        count = read_count(file_path)
        logging.info(f"Read current count: {count}")
        new_count = increment_count(count)
        logging.info(f"Incremented count: {new_count}")
        write_count(file_path, new_count)
        logging.info("Wrote new count to file")
    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse(str(-1), status_code=400)
    return func.HttpResponse(str(count), status_code=200)