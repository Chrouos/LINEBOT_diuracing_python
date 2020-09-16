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
from custom_models import utils, diuracingTalk

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

# 紀錄資料
@handler.add(MessageEvent, message=TextMessage)
def reply_text_message(event):
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        
        reply = False
        
        #if not reply:
        #    reply = diuracingTalk.insert_record(event)

        if not reply:
            reply = diuracingTalk.insert_record(event)

        if not reply:
            reply = diuracingTalk.google_isch(event)
                    
        if not reply:
            reply = diuracingTalk.echo(event)




if __name__ == "__main__":
	app.run()