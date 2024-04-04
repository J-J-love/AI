import requests

API_URL = 'https://model-app-func-modelscc-ebbbfc-ymsqftrsrm.cn-shanghai.fcapp.run/invoke'


def post_request(url, json):
    with requests.Session() as session:
        response = session.post(url, json=json, )
        return response


payload = {"input": {"text": "A panda eating bamboo on a rock."}}
response = post_request(API_URL, json=payload)
print("response:", response.json())
