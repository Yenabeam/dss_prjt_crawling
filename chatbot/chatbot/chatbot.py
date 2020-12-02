from flask import Flask, request, Response 
import libs.naver as naver
import libs.slack as slack
import libs.fleafully as fleafully

from config import Config

app = Flask(__name__)

app.config.from_object(Config)

@app.route("/")
def index():
    return "server is running!"

@app.route("/bot", methods=['POST'])
def bot():
    
    username = request.form.get('user_name')
    token = request.form.get('token')
    text = request.form.get('text')
    
    print(username, token, text)
    
    # 문장 형식이 맞는지 확인
    if text.find(":") < 0:
        msg = """(명령):(데이터) 포멧으로 입력해주세요. :robot_face:
        
명령어 예시)
        
        !bot 정보:
        !bot 추천:
        !bot 시세:100
        !bot 인치:13
        !bot 지역:서울
        """
        slack.send_msg(Config.webhook_url, msg)
        return Response(), 200
    
    # 명령 문자열에 따라서 코드 실행
    comm, data = text.split(":")[0], text.split(":")[1]
    
    if "번역" in comm:
        msg = naver.translate(Config.naver_id, Config.naver_secret, data)
        slack.send_msg(Config.webhook_url, msg)
    elif "시세" in comm:
        msg = fleafully.count(data)
        slack.send_msg(Config.webhook_url, msg)
    elif "인치" in comm:
        msg = fleafully.inch(data)
        slack.send_msg(Config.webhook_url, msg)
    elif "정보" in comm:
        msg = "TOP4 중고 마켓 매물을 한눈에 보자! :eyes: \n http://fleafully.com/"
        slack.send_msg(Config.webhook_url, msg)    
    elif "지역" in comm:
        msg = fleafully.locate(data)
        slack.send_msg(Config.webhook_url, msg)
    elif "추천" in comm:
        msg = fleafully.suggest()
        slack.send_msg(Config.webhook_url, msg)
    else:
        msg = "{}은(는)없는 명령입니다.".format(comm)
        
    return Response(), 200

app.run(debug=True)
