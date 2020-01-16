# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:45:40 2020

@author: tie305403
"""

from flask import Flask, render_template, jsonify
#from flask_restplus import Api, Resource, fields

app = Flask(__name__)
#api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

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
    mem_id : string
        会員を管理するユニークID。
    password : string
        会員に紐づくパスワード。

    Returns
    -------
    auth_result : int
        認証結果。ログインが成功したかを確認するフラグ。'0'：成功 '1'：失敗
    session_id : string
        セッションID 0faa025f
    """

    auth_result = 0
    session_id = '0faa025f'
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
    session_id : string
        セッションID 0faa025f

    Returns
    -------
    auth_result : int
        認証結果。ログインが成功したかを確認するフラグ。'0'：成功 '1'：失敗 '2'：XX
    customer_info : dict
        照会結果  ユーザの情報。指名、生年月日、住所、メールアドレス、電話番号
    """
    auth_result = 0
    customer_info = {}
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
    session_id : string
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
    auth_result = 0
    ask_result = 0
    balance_info = {}
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
    session_id : string
        セッションID 0faa025f

    Returns
    -------
    auth_result : int
        認証結果。ログインが成功したかを確認するフラグ。'0'：成功 '1'：失敗 '2'：XX
    ask_result : int
        照会結果  '0'：成功 '1'：失敗 '2'：未実行
    detail_info : dict
        利用明細。ご利用年月日、ご利用場所、ご利用金額、支払方法
    """
    auth_result = 0
    ask_result = 0
    detail_info = {}
    return jsonify({'auth_result': auth_result, 'ask_result': ask_result, 'detail_info': detail_info})

if __name__ == "__main__":
    app.run(debug=True, port=5000, threaded=True)