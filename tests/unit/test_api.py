import json
import pytest
from function.push import __api_get_access_token
from function.push import __api_send
from function.push import APIReturnCode


def test_get_access_token():
    code, _ = __api_get_access_token()
    assert code == APIReturnCode.OK


def test_send():
    access_token = "aa"
    data = {
        "chatid": "aa",
        "msgtype": "markdown",
        "markdown": {
            "content": "test"
        }
    }
    code, _ = __api_send(
        json.dumps(data), access_token)
    assert code == APIReturnCode.OK
