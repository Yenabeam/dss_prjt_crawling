import requests
import time
import re
import configparser
from selenium import webdriver
# from fake_useragent import UserAgent


def create_token():
    
    config = configparser.ConfigParser()
    config.read('/home/ubuntu/masterpiece/kakao_api.ini')
    kakao_api = config["kakao"]

    API_KEY = kakao_api['rest_api']
    REDIRECT_URI = "https://fastcampus.co.kr/oauth"
    url = "https://kauth.kakao.com/oauth/authorize?client_id={}&redirect_uri={}&response_type=code".format(
        API_KEY, REDIRECT_URI)

    # login - selenium
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36")
    options.add_argument("headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)

    email = kakao_api["email"]
    pw = kakao_api["pw"]
    driver.find_element_by_css_selector('#id_email_2').send_keys(email)
    driver.find_element_by_css_selector('#id_password_3').send_keys(pw)
    driver.find_element_by_css_selector(
        '#login-form > fieldset > div.wrap_btn > button.btn_g.btn_confirm.submit').click()
    time.sleep(2)
    code_url = driver.find_element_by_css_selector(
        'head > meta:nth-child(14)').get_attribute('content')
    driver.quit()

    authorize_code = re.findall('code=(.+)', code_url)

    url = "https://kauth.kakao.com/oauth/token"

    params = {
        "grant_type": "authorization_code",
        "client_id": API_KEY,
        "redirect_uri": REDIRECT_URI,
        "code": authorize_code,
    }
    response = requests.post(url, params)

    user_datas = response.json()

    return user_datas


def refresh_token():
    
    config = configparser.ConfigParser()
    config.read('/home/ubuntu/masterpiece/kakao_api.ini')
    kakao_api = config["kakao"]
    
    API_KEY = kakao_api['rest_api']
    CLIENT_SECRET = kakao_api['client_secret']
    REFRESH_TOKEN = kakao_api['refresh_token']
    user_datas = {'access_token': kakao_api['access_token'],
                  'token_type': 'bearer',
                  'refresh_token': kakao_api['refresh_token'],
                  'expires_in': 21599,
                  'scope': 'talk_message profile',
                  'refresh_token_expires_in': 5183999}

    url = "https://kauth.kakao.com/oauth/token"

    params = {
        "grant_type": "refresh_token",
        "client_id": API_KEY,
        "refresh_token": REFRESH_TOKEN,
        "client_secret": CLIENT_SECRET,
    }

    response = requests.post(url, params)

    refresh_datas = response.json()

    user_datas.update(refresh_datas)

    return user_datas
