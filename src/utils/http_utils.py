from typing import Any

from src.utils.json_utils import json_dumps


def ok_response(response: Any):
    return {
        'statusCode': 200,
        'body': json_dumps(
            response
        )
    }
