import nonebot
import requests

config = nonebot.get_driver().config

secret = config.qq_bots[0]["secret"]
appId = config.qq_bots[0]["id"]
token_get_url = config.qq_bots[0]["token_get_url"]


def get_access_token():
    """
    使用appid和secret获取qq开放平台的access_token
    """
    headers = {"Content-Type": "application/json"}
    data = {"appId": appId, "clientSecret": secret}

    # TODO:容错机制
    response = requests.post(token_get_url, headers=headers, json=data)
    token = response.json()["access_token"]
    return token


def get_authorization_headers():
    token = get_access_token()
    authorization_headers = {
        "Authorization": f"QQBot {token}",
    }

    return authorization_headers
