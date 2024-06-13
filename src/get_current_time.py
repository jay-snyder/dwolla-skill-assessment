from datetime import datetime
import json


def handler(_event, _context):
    return create_json_response(get_current_timestamp())


def get_current_timestamp() -> str:
    return datetime.now().isoformat()


def create_json_response(timestamp: str) -> str:
    response = {"currentTime": timestamp}

    return json.dumps(response)
