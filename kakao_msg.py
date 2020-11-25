def send_msg():
    import requests
    import json

    with open("kakao_code.json", "r") as fp:
        user_datas = json.load(fp)

    url = "https://kapi.kakao.com/v2/user/me"

    headers = {
        "Authorization": "Bearer {}".format(user_datas["access_token"])
    }

    response = requests.get(url, headers=headers)

    msg = "따끈따끈한 중고 매물이 등장했습니다!! 지금 바로 확인하세요!"

    params = {
        "object_type" : "feed",
        "content" : {
            "title" : msg,
            "image_url" : "https://blog.kakaocdn.net/dn/OcEyx/btqDc4487Zt/ZasC1mcegONw6jz2x7wlak/img.jpg",
            "link" : {
                "web_url" : "http://fleafully.com/"
            },        
        },
    }

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    headers = {
        "Content-Type" : "application/x-www-form-urlencoded",
        "Authorization" : "Bearer {}".format(user_datas["access_token"])
    }

    payload = "template_object=" + str(json.dumps(params))
    response = requests.post(url, payload, headers=headers)

    print(response, response.text)