![img](https://user-images.githubusercontent.com/72847093/101735679-91af6b80-3b05-11eb-972b-97d421deff0e.PNG)
# FleaFully, 중고마켓 서비스 개선으로 보다 풍요로운 삶을 제공하다

## 1. 소개 
### 기획 의도, 그리고 우리의 목표 
해를 거듭할수록 증가하는 중고마켓 시장의 데이터를 유저들이 하나의 플랫폼에서 좀 더 편하게 사용할수 있음을 목표로 함
### FleaFully를 통해 무엇을 할 수 있나요?
  - 판매자들은 현재 팔려는 물건들의 시장 매물수와 판매 가격 측정
  - 구매자들은 현재 구매하려는 물품의 시세와 근처 동네의 매물 개수 파악
  - 원하는 품목의 가격을 입력하면 매물이 올라왔을때 메일로 notification 주는 기능
  - 챗봇을 통해 매물 추천과 필터링 기능
  - 인기 카테고리 품목들의 가격 비교
### 이름은 왜 FleaFully 인가요
중고 마켓이라는 Fleamarket과 온전함, 풍부함의 뜻을 가지고 있는 Full을 합쳐서 만든 이름입니다. 
## 2. 시스템 구조
![fleafully-draw_yena](https://user-images.githubusercontent.com/72847093/101736444-bd7f2100-3b06-11eb-9bc0-d75cb7546081.png)
## 3. Contribute 
### Details 
#### Getting Started
#### Prerequisites
#### Dataset 
#### 코드 설명 1 
#### 코드 설명 2
#### 코드 설명 3
#### 코드 설명 2 
- run.py
  - jungonara.py를 12개 카테고리에 대해 실행  후 mongo.py 실행
- jungonara.py
  - 키워드를 입력하면 중고나라에서 크롤링 및 좌표 추출 및 mongodb에 저장
- mongo.py 
  - db 백업, 데이터 전처리 후 챗봇용 collection 생성, 카카오톡과 슬랙에 알림톡 발송, 2시간 단위 db 삭제
- kakao_token.py
  - 카카오 api token을 발급 & 갱신
#### 코드 설명 3
- scrapy.py
  - 당근마켓에서 원하는 키워드 명으로 데이터를 crawling
- pipeline.py
  - 당근마켓에 있는 ~구~동 주소으로 부터 kakao local api를 통해 lat,lon 추출
- jitter.R
  - 정확한 주소가 아니라 ~구~동이라던가 지하철명으로 되있어서 중복 되는 좌표값들이 맵에서 겹쳐보이는 걸 방지하기 위해 jitter함수로 중복값을 변경
- mongodb.py
  - 모은 자료들을 mongoDB에 저장
- get_data.js
  - mongoDB에서 node.js를 통해 json파일 형식의 데이터로 가져옴
- map.html
  - get_data.js를 통해 가져온 데이터를 kakao map api를 통해 맵으로 구현

## 4. Built with 
- 김성준
  - Selenium을 통해 중고나라 크롤링, MongoDB 관리, 슬랙 챗봇 구현, 카카오 api와 슬랙 webhook을 통한 알림톡 발송, 리드미 작성
  - Git hub: https://github.com/alltimeno1
- 전예나 
  - Flask를 통한 AWS 웹 서버 배포, css-js 템플릿을 통한 프론트엔드 구현, 번개장터 크롤링, DB - 웹 연동, 메일 발송 기능 구현, 리드미 작성 
  - Git hub: https://github.com/Yenabeam
- 정하윤 
  - Scrapy Framework를 통해 당근마켓 크롤링, Kakao local api 통해 거래주소에서 lat, lon값 추가, Rscript의 jitter함수를 통해 중복되는 좌표 변경
  - Node.js를 통해 mongodb에서 collection 데이터 import후 kakao map api통해 지도 구현
  - Git hub: https://github.com/hayoon
- 이화진 
  - 기여기여기여기여
  - Git hub: 
## 5. 그리고 
#### 참고사이트 
- 중고나라 : https://www.joongna.com/
- 당근마켓 : https://www.daangn.com/
- 번개장터 : https://m.bunjang.co.kr/
- 헬로마켓 : https://www.hellomarket.com/
#### Q&A
- Contact us :  
###### 본 프로젝트는 패스트캠퍼스 데이터사이언스 취업스쿨 15th 크롤링 프로젝트로 진행되었습니다.
