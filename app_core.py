# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
# serach
import urllib
import re
import random
#import custom_models
from custom_models import utils, diuracingTalk, diuracingPosition

app = Flask(__name__)

# LINE 聊天機器人的基本資料:
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

#Heroku網站
@app.route("/") #GET，並無任何表明所以不需要methods
def home():
    return render_template("home.html")


# 接收 LINE 的資訊:
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    #如果成功就回傳OK
    return 'OK'

# 收到 TextMessage (文字信息)的時候，就執行下列程式碼
@handler.add(MessageEvent, message=TextMessage)
def reply_text_message(event):
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        
        reply = False
        
        if not reply:
            reply = diuracingPosition.position_BaiHuaChi(event)
        if not reply:
            reply = diuracingPosition.position_DaRenCourt(event)
        if not reply:
            reply = diuracingPosition.position_BaiHuaChiSquare(event)
        if not reply:
            reply = diuracingPosition.position_ConfuciusRoad_01(event)
        if not reply:
            reply = diuracingPosition.position_ConfuciusRoad_02(event)
        if not reply:
            reply = diuracingPosition.position_ChristRood_01(event)
        if not reply:
            reply = diuracingPosition.position_ChristRood_02(event)
        if not reply:
            reply = diuracingPosition.position_DaYiSquare(event)
        if not reply:
            reply = diuracingPosition.position_DaYiCourt(event)
        if not reply:
            reply = diuracingPosition.position_DaDian(event)
        if not reply:
            reply = diuracingPosition.position_DaAn(event)
        if not reply:
            reply = diuracingPosition.position_DaGon(event)
        if not reply:
            reply = diuracingPosition.position_DaChen(event)
        if not reply:
            reply = diuracingPosition.position_DaRen(event)
        if not reply:
            reply = diuracingPosition.position_Dayi(event)


        # 如果輸入 「創建角色:」 ，便會開啟資料庫功能
        #if not reply:
        #    reply = diuracingTalk.insert_record(event)

        # 如果輸入「位置」，便會開啟資料庫查詢
        #if not reply:
        #	reply = diuracingTalk.select_position(event)


        # 輸入文字後會自動搜尋圖片
        #if not reply:
        #    reply = diuracingTalk.google_isch(event)
                    
        #若未成功搜尋圖片，便會自動重複回復訊息
        if not reply:
            reply = diuracingTalk.echo(event)




if __name__ == "__main__":
	app.run()