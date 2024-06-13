from datetime import datetime
import json


def handler(_event, _context):
    return create_json_response(200, {"currentTime": get_current_timestamp()})


def get_current_timestamp() -> str:
    return datetime.now().isoformat()


def create_json_response(status_code: int, body: dict) -> str:
    response = {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": body,
    }

    return json.dumps(response)
