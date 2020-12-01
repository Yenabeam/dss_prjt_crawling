from flask import *
import pickle
import os
import numpy as np
from flask import render_template
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
import pymysql
import pymysql.cursors

app = Flask(__name__)
Bootstrap(app)
db = pymysql.connect(host='15.165.128.7',port=3306, user= 'root', password='dss', db='UserInfo',charset='utf8')
cursor = db.cursor()

# 메인 페이지 
@app.route('/')
def main():
    return render_template('main.html')

# 지도 페이지 연결 
@app.route('/map')
def map():
    return render_template('kakaomap.html')

# 가격 비교 사이트 mongo 연결 
@app.route('/list')
def mongoTest():
    client = MongoClient('mongodb://dss:dss@15.165.128.7:27017')
    db = client.joongo
    collection = db.D20112515
    results = collection.find({})
    client.close()
    return render_template('mongo.html', data=results)

#메일 발송 페이지 
@app.route('/mail',methods=['GET'])
def mail():
    return render_template('mail_raw.html')

@app.route('/register', methods=['POST'])
def sendingmail():
    if request.method == 'POST':
        register_info = request.form
        username = register_info['username']
        price = register_info['price']
        email = register_info['email']
        print(username,price,email)
        sql ='''
            INSERT INTO UserInfo (username, price, email)
            VALUES (%s, %s, %s);
        '''
        cursor.execute(sql, (username, price, email))
        db.commit()
        db.close()
        return redirect(request.url)
    return render_template('mail_raw.html')

#메일 발송 페이지_test 
@app.route('/mailtest', methods=['GET'])
def mailtest():
    return render_template('mail_test.html')

@app.route('/mailsubmit', methods=['POST'])
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
        db.close()
        return username
        # return redirect(request.url)
    return render_template('mail_test.html')


app.run(debug=True)
