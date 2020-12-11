import requests
import json

WEBHOOK_URL = "https://hooks.slack.com/services/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"


def send_msg2(msg, channel="#dss", username="중고봇"):
    payload = {"channel": channel, "username": username, "text": msg}
    return requests.post(WEBHOOK_URL, json.dumps(payload))
