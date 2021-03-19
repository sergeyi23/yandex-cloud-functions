import json

from src.models.login_request import LoginRequest
from src.services.account_service import login
from src.utils.http_utils import ok_response


def handler(event, _context):
    # parse request model here
    body = json.loads(event["body"])
    login_request = LoginRequest(body["userName"], body["password"])
    # pass request to business logic for processing
    login_response = login(login_request)
    # send HTTP response
    return ok_response(login_response)
