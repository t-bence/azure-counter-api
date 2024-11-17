import azure.functions as func
import logging
from counter import increment_count, get_response

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="count_visitors")
def count_visitors(req: func.HttpRequest) -> func.HttpResponse: # , input: str, output: func.Out[str]
    logging.info('Python HTTP trigger function processed a request.')

    input = "123"

    try:
        count = int(input)
        logging.info(f"Read current count: {count}")
        new_count = increment_count(count)
        logging.info(f"Incremented count: {new_count}")
        #output.set(str(new_count))
        logging.info("Wrote new count to file")
    except Exception as e:
        logging.error(str(e))
        return get_response(None)
    return get_response(count)