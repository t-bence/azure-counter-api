import json
import azure.functions as func

def increment_count(count: int) -> int:
    return count + 1

def get_response(count: int = None) -> func.HttpResponse:
    value = count if count else -1
    status_code = 200 if count else 400

    return func.HttpResponse(
        json.dumps(dict(visitors=value)),
        status_code=status_code,
        mimetype="application/json"
    )
