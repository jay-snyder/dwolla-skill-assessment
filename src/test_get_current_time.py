from get_current_time import handler
from unittest.mock import patch, Mock


@patch(
    "get_current_time.get_current_timestamp",
    Mock(return_value="2024-06-12T20:04:10.885479"),
)
def test_handler():
    response = handler(None, None)

    assert response == '{"currentTime": "2024-06-12T20:04:10.885479"}'

if __name__ == "__main__":
    test_handler()