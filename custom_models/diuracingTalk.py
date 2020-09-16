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
# 我們的函數
from custom_models import utils, CallDatabase
import psycopg2
import os

app = Flask(__name__)

# LINE 聊天機器人的基本資料:
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


# 請LINEBOT幫我們在GOOGLE找圖片
def google_isch(event):
	# 找圖
	try:
		q_string = {'tbm': 'isch', 'q': event.message.text}
		# url 搜尋的網址，後面加入搜尋的條件
		url = f"https://www.google.com/search?{urllib.parse.urlencode(q_string)}/"
		# 告訴GOOGLE我是誰，比較安全，不容易被阻擋
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

		req = urllib.request.Request(url, headers = headers)
		conn = urllib.request.urlopen(req)

		pattern = 'img data-src="\S*"'
		img_list = []

		for match in re.finditer(pattern, str(conn.read())):
			img_list.append(match.group()[14:-1])

		random_img_url = img_list[random.randint(0, len(img_list)+1)]
		print('fetch img url finish')

		line_bot_api.reply_message(
			event.reply_token,
			ImageSendMessage(
				original_content_url=random_img_url,
				preview_image_url=random_img_url
			)
		)
		return True

	except:
		return False	


# 學說話
def echo(event):
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text=event.message.text)
		#TextSendMessage(text=str(event.source.user_id))
	)
	return True

# 請 LINE 幫我們存入資料，創建帳號密碼
def insert_record(event):
    if '創建角色:' in event.message.text:

        try:
            record_list = utils.prepare_record(event.message.text, event.source.user_id)
            print('LIST OK')

            reply = CallDatabase.line_insert_record(record_list)

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply)
            )

        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='不好意思，此名稱或密碼已有人使用')
            )
        return True

    else:
        return False

def select_position(event):
	if '資料庫位置' in event.message.text:

		try:
			reply = CallDatabase.line_select_overall(event.message.text)
			print('POSITION OK')

			line_bot_api.reply_message(
				event.reply_token,
				TextSendMessage(text=reply)
			)

		except:
			line_bot_api.reply_message(
				event.reply_token,
				TextSendMessage(text='不好意思，位置查詢錯誤，請稍後重試')
			)			

		return True

	else:
		return False	
