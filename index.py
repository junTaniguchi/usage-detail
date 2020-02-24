# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:45:40 2020

@author: tie305403
"""

from flask import Flask, render_template, request, abort, jsonify
import requests

app = Flask(__name__)
#api = Blueprint('api', __name__, url_prefix='/api')

#APIサーバ名称
URL_ITEMS = 'http://localhost:5001'
#セッションID
session_id = ''

@app.route('/')
def index():
    return "hello"

@app.route('/api/login/', methods=['POST'])
def post_login():
    """
    ログイン認証

    APIコール元から会員番号、パスワード、セッションキーを受領し、データベース上の会員情報と照合する。
    照合に成功した場合、認証結果'0'とセッションキーから生成した（ハッシュ関数のような）セッションIDを返却する。
    セッションIDは、後続で呼び出されるAPIの引数として、ログイン認証の簡略化に使用される。

    照合に失敗した場合、認証結果'1'のみ返却する。
    エラー理由に関わらず、ログイン画面でのエラーメッセージは「IDまたはパスワードが誤っています」とする。

    Parameters
    ----------
    mem_id : str
        会員を管理するユニークID。
    password : str
        会員に紐づくパスワード。

    Returns
    -------
    auth_result : int
        認証結果。ログインが成功したかを確認するフラグ。'0'：成功 '1'：失敗
    session_id : str
        セッションID 0faa025f
    """
    headers = {'Authorization': 'Bearer {}'.format('a')}
    payload = request.json
    mem_id = payload.get('mem_id')
    password = payload.get('password')

    #if not mem_id or not password:
    #    abort(404, {'auth_result': '1', 'session_id': null})

    #payload作成
    item_data = {
        'mem_id'   : mem_id,
        'password' : password
    }
    #API Call
    #req_post = requests.post(URL_ITEMS, headers=headers, json=item_data)
    #セッションIDをサーバ側で保持
    #session_id = req_post.json()['session_id']
    #auth_result = req_post.json()['auth_result']
    
    session_id = '0faa025f'
    auth_result = 0
    return jsonify({'auth_result': auth_result, 'session_id': session_id})

@app.route('/api/get/user/<string:session_id>', methods=['GET'])
def get_customer(session_id=None):
    """
    顧客情報照会

    APIコール元からセッション、会員番号を受領し、データベース上のセッション情報と照合する。
    セッションIDによる認証に成功した場合は、認証結果'0'を設定し、セッションIDに紐づく会員番号で顧客情報を検索する。
    セッションIDによる認証に失敗した場合は、認証結果'1'と照会結果'2'を設定し、データを返却する。

    Parameters
    ----------
    session_id : str
        セッションID 0faa025f

    Returns
    -------
    auth_result : int
        認証結果。ログインが成功したかを確認するフラグ。'0'：成功 '1'：失敗 '2'：XX
    customer_info : dict
        照会結果  ユーザの情報。指名、生年月日、住所、メールアドレス、電話番号
    """

    #if not session_id:
    #    abort(404, {'auth_result': '1', 'customer_info': null})

    #API Call
    headers = {'Authorization': 'Bearer {}'.format('a')}
    #req_get = requests.get(URL_ITEMS + '/api/get/user/' + session_id, headers=headers)
    #auth_result = req_get.json()['auth_result']
    #customer_info = req_get.json()['customer_info']

    auth_result = 0
    customer_info = {
        'user_name' : 'TIS株式会社',
        'birthday'  : '20080401',
        'address'   : '東京都新宿区西新宿8丁目17番1号住友不動産新宿グランドタワー',
        'email'     : 'XXXXX@tis.co.jp',
        'phone'     : '03-5337-7070'
    }
    return jsonify({'auth_result': auth_result, 'customer_info': customer_info})

@app.route('/api/get/balance/<string:session_id>', methods=['GET'])
def get_balance(session_id=None):
    """
    残高照会

    APIコール元からセッションIDを受領し、データベース上のセッション情報と照合する。
    セッションIDによる認証に成功した場合は、認証結果'0'を設定し、セッションIDに紐づく会員番号で残高情報を検索する。
    セッションIDによる認証に失敗した場合は、認証結果'1'と照会結果'2'を設定し、データを返却する。

    残高情報の検索に成功した場合は、照会結果'0'と残高情報（0～1の項目）を設定し、データを返却する。
    残高情報の検索に失敗した場合は、照会結果'1'を設定し、データを返却する。
    
    Parameters
    ----------
    session_id : str
        セッションID 0faa025f

    Returns
    -------
    auth_result : int
        認証結果。ログインが成功したかを確認するフラグ。'0'：成功 '1'：失敗
    ask_result : int
        照会結果  '0'：成功 '1'：失敗 '2'：未実行
    balance_info : dict
        残高情報。総枠、割賦枠、CS枠、総利用額、割賦利用額、CS利用額、総利用残高、割賦利用残高、CS利用残高
    """

    #if not session_id:
    #    abort(404, {'auth_result': '1', 'ask_result': 2, 'balance_info': null})

    #API Call
    #headers = {'Authorization': 'Bearer {}'.format('a')}
    #req_get = requests.get(URL_ITEMS + '/api/get/balance/' + session_id, headers=headers)
    #auth_result = req_get.json()['auth_result']
    #ask_result = req_get.json()['ask_result']
    #balance_info = req_get.json()['balance_info']

    auth_result = 0
    ask_result = 0
    
    balance_info = {
        'total' : {
            'all' : {
                'frame'		: 1000000,
                'usage'		: 600000,
                'balance'	: 400000,
            },
            'sp' : {
                'frame'		: 1000000,
                'usage'		: 250000,
                'balance'	: 300000,
            },
            'installment' : {
                'frame'		: 500000,
                'usage'		: 200000,
                'balance'	: 300000,
            },
            'cs' : {
                'frame'		: 500000,
                'usage'		: 150000,
                'balance'	: 350000,
            }
        },
        'installment' : {
            'all' : {
                'frame'		: 500000,
                'usage'		: 200000,
                'balance'	: 300000,
            },
            'twice' : {
                'frame'		: 200000,
                'usage'		: 50000,
                'balance'	: 150000,
            },
            'manytimes' : {
                'frame'		: 200000,
                'usage'		: 50000,
                'balance'	: 150000,
            },
            'bonus' : {
                'frame'		: 200000,
                'usage'		: 50000,
                'balance'	: 150000,
            },
            'revolving' : {
                'frame'		: 200000,
                'usage'		: 50000,
                'balance'	: 150000,
            },
        },
        'cs' : {
            'all' : {
                'frame'		: 500000,
                'usage'		: 150000,
                'balance'	: 350000,
            },
            'domestic' : {
                'frame'		: 300000,
                'usage'		: 50000,
                'balance'	: 300000,
            },
            'overseas' : {
                'frame'		: 300000,
                'usage'		: 50000,
                'balance'	: 300000,
            },
            'revolving' : {
                'frame'		: 300000,
                'usage'		: 50000,
                'balance'	: 300000,
            },
        },
    }
    
    return jsonify({'auth_result': auth_result, 'ask_result': ask_result, 'balance_info': balance_info})

@app.route('/api/get/details/<string:session_id>', methods=['GET'])
def get_details(session_id=None):
    """
    ご利用明細照会

    APIコール元からセッションIDとページ数を受領し、データベース上のセッション情報と照合する。
    セッションIDによる認証に成功した場合は、認証結果'0'を設定し、セッションIDに紐づく会員番号でご利用明細情報を検索する。
    セッションIDによる認証に失敗した場合は、認証結果'1'と照会結果'2'を設定し、データを返却する。

    ご利用明細情報の検索に成功した場合は、照会結果'0'とご利用明細情報（0～1の項目）を設定する。
    引数のページ数が'01'のときのご利用明細情報は、ご利用年月日の降順でソートして1～10件目を設定する。
    引数のページ数に応じて、設定するご利用明細書情報の対象が10件単位で変化する。
    ご利用明細が存在しない（カード利用がない）場合は、ご利用明細情報は設定しない。
    
    Parameters
    ----------
    session_id : str
        セッションID 0faa025f

    Returns
    -------
    auth_result : int
        認証結果。ログインが成功したかを確認するフラグ。'0'：成功 '1'：失敗
    ask_result : int
        照会結果  '0'：成功 '1'：失敗 '2'：未実行
    detail_info : dict
        利用明細。ご利用年月日、ご利用場所、ご利用金額、支払方法
    """

    #if not session_id:
    #    abort(404, {'auth_result': '1', 'ask_result': 2, 'balance_info': null})

    #API Call
    #headers = {'Authorization': 'Bearer {}'.format('a')}
    #req_get = requests.get(URL_ITEMS + '/api/get/details/' + session_id, headers=headers)
    #auth_result = req_get.json()['auth_result']
    #ask_result = req_get.json()['ask_result']
    #detail_info = req_get.json()['detail_info']

    auth_result = 0
    ask_result = 0
    detail_info = [
        {
            'record_no'   : 1,
            'usage_date'  : '20080401',
            'usage_shop'  : 'd社',
            'usage_amount': 100,
            'method'      : 'card'
        },
        {
            'record_no'   : 2,
            'usage_date'  : '20080401',
            'usage_shop'  : 'k社',
            'usage_amount': 1,
            'method'      : 'card'
        }
    ]
    return jsonify({'auth_result': auth_result, 'ask_result': ask_result, 'detail_info': detail_info})

@app.route('/api/get/chart/<string:session_id>', methods=['GET'])
def get_chart(session_id=None):
    """
    ご利用明細照会

    APIコール元からセッションIDとページ数を受領し、データベース上のセッション情報と照合する。
    セッションIDによる認証に成功した場合は、認証結果'0'を設定し、セッションIDに紐づく会員番号でご利用明細情報を検索する。
    セッションIDによる認証に失敗した場合は、認証結果'1'と照会結果'2'を設定し、データを返却する。

    ご利用明細情報の検索に成功した場合は、照会結果'0'とご利用明細情報（0～1の項目）を設定する。
    引数のページ数が'01'のときのご利用明細情報は、ご利用年月日の降順でソートして1～10件目を設定する。
    引数のページ数に応じて、設定するご利用明細書情報の対象が10件単位で変化する。
    ご利用明細が存在しない（カード利用がない）場合は、ご利用明細情報は設定しない。
    
    Parameters
    ----------
    session_id : str
        セッションID 0faa025f

    Returns
    -------
    auth_result : int
        認証結果。ログインが成功したかを確認するフラグ。'0'：成功 '1'：失敗
    ask_result : int
        照会結果  '0'：成功 '1'：失敗 '2'：未実行
    detail_info : dict
        利用明細。ご利用年月日、ご利用場所、ご利用金額、支払方法
    """

    #if not session_id:
    #    abort(404, {'auth_result': '1', 'ask_result': 2, 'balance_info': null})

    #API Call
    #headers = {'Authorization': 'Bearer {}'.format('a')}
    #req_get = requests.get(URL_ITEMS + '/api/get/details/' + session_id, headers=headers)
    #auth_result = req_get.json()['auth_result']
    #ask_result = req_get.json()['ask_result']
    #detail_info = req_get.json()['detail_info']

    auth_result = 0
    ask_result = 0
    chart_data = {
        '外食':{
            'スターバックスコーヒー': [
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
            ],
            '蒙古タンメン仲本': [
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
            ]
        },
        '医療薬品':{
            '市ヶ谷歯科クリニック': [
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
            ],
            'マツモトキヨシ': [
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
            ]
        },
        'ホテル': {
            'ニューオータニ': [
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
            ],
            'HILTON': [
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
            ]
        },
        'エンターテイメント': {
            'TOHOシネマズ': [
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
                { '利用日':'2018/04/01', 'ご利用額': 1000 },
            ],
            '伊勢丹': {
                'ルイヴィトン': [
                    { '利用日':'2018/04/01', 'ご利用額': 1000 },
                    { '利用日':'2018/04/01', 'ご利用額': 1000 },
                    { '利用日':'2018/04/01', 'ご利用額': 1000 },
                ],
                '資生堂': [
                    { '利用日':'2018/04/01', 'ご利用額': 1000 },
                    { '利用日':'2018/04/01', 'ご利用額': 1000 },
                    { '利用日':'2018/04/01', 'ご利用額': 1000 },
                ],
                '伊勢丹': [
                    { '利用日':'2018/04/01', 'ご利用額': 1000 },
                    { '利用日':'2018/04/01', 'ご利用額': 1000 },
                    { '利用日':'2018/04/01', 'ご利用額': 1000 },
                ]
            }
        }
    };
    return jsonify({'auth_result': auth_result, 'ask_result': ask_result, 'chart_data': chart_data})

if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)
