from datetime import datetime
import json


def handler(_event, _context):
    return create_response(200, {"currentTime": get_current_time()})


def get_current_time() -> str:
    return datetime.now().isoformat()


def create_response(status_code: int, body: dict) -> str:
    response = {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": body,
    }

    return json.dumps(response)
