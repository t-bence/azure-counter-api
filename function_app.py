import azure.functions as func
import logging
from counter import increment_count, get_response

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

"""
@app.blob_output(arg_name="output",
                path="visitors/count.txt",
                connection="CounterStorage")
                """

@app.route(route="count_visitors")
@app.blob_input(arg_name="input",
                path="visitors/count.txt",
                connection="CounterStorage")

def count_visitors(req: func.HttpRequest, input: str) -> func.HttpResponse: #output: func.Out[str]
    logging.info('Python HTTP trigger function processed a request.')

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