from flask import *
import pickle
import os
import numpy as np
from flask import render_template
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
import pymysql
import pymysql.cursors
import time
from datetime import datetime


app = Flask(__name__)
Bootstrap(app)
db = pymysql.connect(host='15.165.128.7',port=3306, user= 'root', password='dss', db='UserInfo',charset='utf8')
cursor = db.cursor()

# 메인 페이지 
@app.route('/')
def main():
    return render_template('main.html')

#카테고리
@app.route('/category')
def category():
    return render_template('category.html')

#카테고리 - no1
today = datetime.now()
@app.route('/no1')
def no1():
    client = MongoClient('mongodb://dss:dss@3.35.98.5:27017')
    db = client.joongo
    collection = db['C{}'.format(today.strftime('%y%m%d%H'))]
    results = collection.find({'keyword':'자전거'}).sort('price')
    client.close()
    return render_template('mongo.html', data=results)

#카테고리 - no2
today = datetime.now()
@app.route('/no2')
def no2():
    client = MongoClient('mongodb://dss:dss@3.35.98.5:27017')
    db = client.joongo
    collection = db['C{}'.format(today.strftime('%y%m%d%H'))]
    results = collection.find({'keyword':'패딩'}).sort('price')
    client.close()
    return render_template('mongo.html', data=results)

#카테고리 - no3
today = datetime.now()
@app.route('/no3')
def no3():
    client = MongoClient('mongodb://dss:dss@3.35.98.5:27017')
    db = client.joongo
    collection = db['C{}'.format(today.strftime('%y%m%d%H'))]
    results = collection.find({'keyword':'노트북'}).sort('price')
    client.close()
    return render_template('mongo.html', data=results)

#카테고리 - no4
today = datetime.now()
@app.route('/no4')
def no4():
    client = MongoClient('mongodb://dss:dss@3.35.98.5:27017')
    db = client.joongo
    collection = db['C{}'.format(today.strftime('%y%m%d%H'))]
    results = collection.find({'keyword':'의자'}).sort('price')
    client.close()
    return render_template('mongo.html', data=results)


#카테고리 - no5
today = datetime.now()
@app.route('/no5')
def no5():
    client = MongoClient('mongodb://dss:dss@3.35.98.5:27017')
    db = client.joongo
    collection = db['C{}'.format(today.strftime('%y%m%d%H'))]
    results = collection.find({'keyword':'아이폰'}).sort('price')
    client.close()
    return render_template('mongo.html', data=results)


#카테고리 - no6
today = datetime.now()
@app.route('/no6')
def no6():
    client = MongoClient('mongodb://dss:dss@3.35.98.5:27017')
    db = client.joongo
    collection = db['C{}'.format(today.strftime('%y%m%d%H'))]
    results = collection.find({'keyword':'아이패드'}).sort('price')
    client.close()
    return render_template('mongo.html', data=results)


#카테고리 - no7
today = datetime.now()
@app.route('/no7')
def no7():
    client = MongoClient('mongodb://dss:dss@3.35.98.5:27017')
    db = client.joongo
    collection = db['C{}'.format(today.strftime('%y%m%d%H'))]
    results = collection.find({'keyword':'캠핑'}).sort('price')
    client.close()
    return render_template('mongo.html', data=results)

#카테고리 - no8
today = datetime.now()
@app.route('/no8')
def no8():
    client = MongoClient('mongodb://dss:dss@3.35.98.5:27017')
    db = client.joongo
    collection = db['C{}'.format(today.strftime('%y%m%d%H'))]
    results = collection.find({'keyword':'냉장고'}).sort('price')
    client.close()
    return render_template('mongo.html', data=results)

#카테고리 - no9
today = datetime.now()
@app.route('/no9')
def no9():
    client = MongoClient('mongodb://dss:dss@3.35.98.5:27017')
    db = client.joongo
    collection = db['C{}'.format(today.strftime('%y%m%d%H'))]
    results = collection.find({'keyword':'컴퓨터'}).sort('price')
    client.close()
    return render_template('mongo.html', data=results)

#카테고리 - no10
today = datetime.now()
@app.route('/no10')
def no10():
    client = MongoClient('mongodb://dss:dss@3.35.98.5:27017')
    db = client.joongo
    collection = db['C{}'.format(today.strftime('%y%m%d%H'))]
    results = collection.find({'keyword':'난로'}).sort('price')
    client.close()
    return render_template('mongo.html', data=results)


#카테고리 - no11
today = datetime.now()
@app.route('/no11')
def no11():
    client = MongoClient('mongodb://dss:dss@3.35.98.5:27017')
    db = client.joongo
    collection = db['C{}'.format(today.strftime('%y%m%d%H'))]
    results = collection.find({'keyword':'에어팟'}).sort('price')
    client.close()
    return render_template('mongo.html', data=results)

#카테고리 - no12
today = datetime.now()
@app.route('/no12')
def no12():
    client = MongoClient('mongodb://dss:dss@3.35.98.5:27017')
    db = client.joongo
    collection = db['C{}'.format(today.strftime('%y%m%d%H'))]
    results = collection.find({'keyword':'모니터'}).sort('price')
    client.close()
    return render_template('mongo.html', data=results) 


#------------지도 페이지 연결 -------------
@app.route('/map')
def map():
    return render_template('kakaomap.html')

#-------------가격 비교 사이트 mongo 연결 --------------
@app.route('/list')
def mongoTest():
    client = MongoClient('mongodb://dss:dss@3.35.98.5:27017')
    db = client.joongo
    collection = db['D{}'.format(today.strftime('%y%m%d%H'))]
    results = collection.find({}).sort('price')
    client.close()
    return render_template('mongo.html', data=results) 

#------------map json 파일 ------------
@app.route('/json')
def json():
    return render_template('data.json') 


#------------메일 발송 페이지------------
@app.route('/mail', methods=['GET'])
def mailtest():
    return render_template('mail_test.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # register_info = request.form
        username = request.form['username']
        price = request.form['price']
        email = request.form['email']
        print(username,price,email)
        sql ='''
            INSERT INTO UserInfo (username, price, email)
            VALUES (%s, %s, %s);
        '''
        cursor.execute(sql, (username, price, email))
        db.commit()
        # db.close()

        return 'done!'
        # return redirect(request.url)
    return render_template('mail_test.html')


app.run(debug=True)
