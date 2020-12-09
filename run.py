from jungonara import overview
from mongo import load_db

categories = ["맥북 프로", "자전거", "패딩", "노트북", "의자", "아이폰", "아이패드",
              "캠핑", "냉장고", "컴퓨터", "에어팟", "모니터"]

for category in categories:
    overview(category)

load_db()
