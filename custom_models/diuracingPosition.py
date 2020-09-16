# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, FlexSendMessage
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

positionCodename = []

if len(positionCodename):
	print("nothing!!")
else:
	positionCodename.append(5)

def position_BaiHuaChi(event):

	if '百花池' in event.message.text:
		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(alt_text='porn template', contents = {"type":"bubble","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"百花池","align":"center","gravity":"top","weight":"bold"}]},"hero":{"type":"image","url":"https://activity.pccu.edu.tw/ezfiles/35/1035/img/1231/171601401.jpg","size":"5xl","aspectRatio":"20:13","aspectMode":"cover"},"body":{"type":"box","layout":"vertical","spacing":"xs","contents":[{"type":"text","text":"百花池的小波紋中，水中倒影清晰可見。池中的石頭上還有一隻可愛的綠色長頸鹿。","size":"sm","weight":"bold","wrap":True},{"type":"button","action":{"type":"message","label":"往大仁館","text":"大仁館"},"color":"#AAAAAA","height":"sm","style":"primary","gravity":"top"},{"type":"button","action":{"type":"message","label":"往百花池廣場","text":"百花池廣場"}},{"type":"button","action":{"type":"message","label":"往基督大道","text":"基督大道"}}]},"footer":{"type":"box","layout":"vertical","spacing":"sm","contents":[{"type":"text","text":"現在有10人在這裡","align":"center","wrap":True},{"type":"button","action":{"type":"message","label":"留言板","text":"百花池留言板"}}]}})
		)	
		positionCodename[-1] = 1
		return True
	else:
		return False


def position_BaiHuaChiSquare(event):

	if '百花池廣場' in event.message.text:
		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(alt_text='porn template', contents = {"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"百花池廣場","align":"center"}]},"hero":{"type":"image","url":"https://pic.pimg.tw/b03050ia/1542459189-1753985712_wn.jpg","size":"full","aspectRatio":"1.51:1","aspectMode":"fit"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"階梯式的座位，寬闊的廣場，校內許多活動都在這裡舉辦!","align":"center","wrap":True},{"type":"button","action":{"type":"message","label":"往百花池","text":"百花池"}},{"type":"button","action":{"type":"message","label":"往孔子大道","text":"孔子大道01"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"現在有15人在這裡","align":"center"},{"type":"button","action":{"type":"message","label":"留言板","text":"百花池廣場留言板"},"gravity":"center"}]}})
		)	
		positionCodename[-1] = 1
		return True
	else:
		return False

def position_ConfuciusRoad_01(event):

	if '孔子大道01' in event.message.text:
		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(alt_text='porn template', contents = {"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"孔子大道","align":"center"}]},"hero":{"type":"image","url":"https://2.blog.xuite.net/2/b/0/5/15196480/blog_359116/txt/53985548/0.jpg","size":"full","aspectRatio":"1.51:1","aspectMode":"fit"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"中國文化以孔子學說為中心，是東方文化的柱石。","align":"center","wrap":True},{"type":"button","action":{"type":"message","label":"往前走","text":"基督大道02"}},{"type":"button","action":{"type":"message","label":"往大恩館","text":"大恩館"}},{"type":"button","action":{"type":"message","label":"往百花池廣場","text":"百花池廣場"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"現在有25人在這裡","align":"center"}]}})
		)	
		positionCodename[-1] = 1
		return True
	else:
		return False	

def position_ConfuciusRoad_02(event):

	if '孔子大道02' in event.message.text:
		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(alt_text='porn template', contents = {"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"孔子大道","align":"center"}]},"hero":{"type":"image","url":"https://pic.pimg.tw/b03050ia/1542459188-982154855_n.jpg","size":"full","aspectRatio":"1.51:1","aspectMode":"fit"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"文化大學中，學生們最常經過的道路，不僅連接百花池廣場，更是連結辦公大樓及教學大樓。","align":"center","wrap":True},{"type":"button","action":{"type":"message","label":"往前走","text":"孔子大道01"}},{"type":"button","action":{"type":"message","label":"往大典館","text":"大典館"}},{"type":"button","action":{"type":"message","label":"往大義館","text":"大義館"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"現在有15人在這裡","align":"center"},{"type":"button","action":{"type":"message","label":"留言板","text":"百花池廣場留言板"},"gravity":"center"}]}})
		)	
		positionCodename[-1] = 1
		return True
	else:
		return False

def position_DaChen(event):

	if '大成館' in event.message.text:
		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(alt_text='porn template', contents = {"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"大成館","align":"center"}]},"hero":{"type":"image","url":"https://cdn2.ettoday.net/images/205/d205613.jpg","size":"full","aspectRatio":"1.51:1","aspectMode":"fit"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"建築平面為「器」字型的城坊式建築，上覆綠色琉璃瓦，頗有古代宮廷式建築的外觀。","align":"center","wrap":True},{"type":"button","action":{"type":"message","label":"往大義球場","text":"大義球場"}},{"type":"button","action":{"type":"message","label":"往基督大道","text":"基督大道02"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"現在有54個人在這裡","align":"center"},{"type":"button","action":{"type":"message","label":"留言板","text":"大成館留言板"}}]}})
		)	
		positionCodename[-1] = 1
		return True
	else:
		return False

def position_Dayi(event):
	if '大義館' in event.message.text:
		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(alt_text='porn template', contents = {"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"大義館","align":"center"}]},"hero":{"type":"image","url":"https://pic.pimg.tw/adrey811/1409791711-444852085.jpg","size":"full","aspectRatio":"1.51:1","aspectMode":"fit"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"格局方正，頂樓為天壇式造型，一樓為全年開放之24小時K書中心。頂樓西面又名「觀海樓」。","align":"center","wrap":True},{"type":"button","action":{"type":"message","label":"往孔子大道","text":"孔子大道02"}},{"type":"button","action":{"type":"message","label":"往大義館廣場","text":"大義館廣場"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"現在有15人在這裡","align":"center"},{"type":"button","action":{"type":"message","label":"留言板","text":"百花池廣場留言板"},"gravity":"center"}]}})
		)	
		positionCodename[-1] = 1
		return True
	else:
		return False


def position_DaRen(event):
	if '大仁館' in event.message.text:
		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(alt_text='porn template', contents = {"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"大義館","align":"center"}]},"hero":{"type":"image","url":"https://pic.pimg.tw/adrey811/1409791711-444852085.jpg","size":"full","aspectRatio":"1.51:1","aspectMode":"fit"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"格局方正，頂樓為天壇式造型，一樓為全年開放之24小時K書中心。頂樓西面又名「觀海樓」。","align":"center","wrap":True},{"type":"button","action":{"type":"message","label":"往孔子大道","text":"孔子大道02"}},{"type":"button","action":{"type":"message","label":"往大義館廣場","text":"大義館廣場"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"現在有15人在這裡","align":"center"},{"type":"button","action":{"type":"message","label":"留言板","text":"百花池廣場留言板"},"gravity":"center"}]}})
		)	
		positionCodename[-1] = 1
		return True
	else:
		return False


def position_ChristRood_01(event):
	if '基督大道01' in event.message.text:
		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(alt_text='porn template', contents = {"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"基督大道","align":"center"}]},"hero":{"type":"image","url":"https://defzd6kpftjvs.cloudfront.net/cf_forum/201302/2013021910141965154b.jpg","size":"full","aspectRatio":"1.51:1","aspectMode":"fit"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"學生們一下課便會經過基督大道，是前往球場或公車站牌的常見道路","align":"center","wrap":True},{"type":"button","action":{"type":"message","label":"往前走","text":"基督大道02"}},{"type":"button","action":{"type":"message","label":"往百花池","text":"百花池"}},{"type":"button","action":{"type":"message","label":"往大成館","text":"大成館"}},{"type":"button","action":{"type":"message","label":"往大義館廣場","text":"大義館廣場"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"現在有25人在這裡","align":"center"}]}})
		)	
		positionCodename[-1] = 1
		return True
	else:
		return False

def position_ChristRood_02(event):
	if '基督大道02' in event.message.text:
		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(alt_text='porn template', contents = {"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"基督大道","align":"center"}]},"hero":{"type":"image","url":"https://defzd6kpftjvs.cloudfront.net/cf_forum/201302/2013021910141965154b.jpg","size":"full","aspectRatio":"1.51:1","aspectMode":"fit"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"旁邊就是公車站牌了，球場上依舊熱鬧，許多人在旁邊圍觀、聊天、加油打氣，許多校內比賽都會在旁邊的球場上進行。","align":"center","wrap":True},{"type":"button","action":{"type":"message","label":"往前走","text":"基督大道01"}},{"type":"button","action":{"type":"message","label":"往大仁球場","text":"大仁球場"}},{"type":"button","action":{"type":"message","label":"往大仁館","text":"大仁館"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"現在有15人在這裡","align":"center"},{"type":"button","action":{"type":"message","label":"留言板","text":"百花池廣場留言板"},"gravity":"center"}]}})
		)	
		positionCodename[-1] = 1
		return True
	else:
		return False

def position_DaYiSquare(event):
	if '大義館廣場' in event.message.text:
		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(alt_text='porn template', contents = {"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"大義館廣場","align":"center"}]},"hero":{"type":"image","url":"https://pic.pimg.tw/b03050ia/1542459186-3783613213_n.jpg","size":"full","aspectRatio":"1.51:1","aspectMode":"fit"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"通過廣場，可以前往學生們午餐去處的美食街，偶爾也會有人來這邊辦活動擺攤等等。","align":"center","wrap":True},{"type":"button","action":{"type":"message","label":"往基督大道","text":"基督大道01"}},{"type":"button","action":{"type":"message","label":"往大義球場","text":"大義球場"}},{"type":"button","action":{"type":"message","label":"往大義館","text":"大義館"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"現在有15人在這裡","align":"center"},{"type":"button","action":{"type":"message","label":"留言板","text":"百花池廣場留言板"},"gravity":"center"}]}})
		)	
		positionCodename[-1] = 1
		return True
	else:
		return False

def position_DaYiCourt(event):
	if '大義球場' in event.message.text:
		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(alt_text='porn template', contents = {"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"大義球場","align":"center"}]},"hero":{"type":"image","url":"https://ddwgnufeodrv4.cloudfront.net/10000957/20181114/1542169726791_plus1_530.jpg","size":"full","aspectRatio":"1.51:1","aspectMode":"fit"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"為球場之一，白天是體育課的好場所，夜晚開始的時候，也會有許多人在這邊打球、聊天。","align":"center","wrap":True},{"type":"button","action":{"type":"message","label":"往大成館","text":"大成館"}},{"type":"button","action":{"type":"message","label":"往大義館廣場","text":"大義館廣場"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"現在有15人在這裡","align":"center"},{"type":"button","action":{"type":"message","label":"留言板","text":"百花池廣場留言板"},"gravity":"center"}]}})
		)	
		positionCodename[-1] = 1
		return True
	else:
		return False

def position_DaDian(event):
	if '大典館' in event.message.text:
		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(alt_text='porn template', contents = {"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"大典館","align":"center"}]},"hero":{"type":"image","url":"https://www.upmedia.mg/upload/article/20190306174126383209.png","size":"full","aspectRatio":"1.51:1","aspectMode":"fit"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"明堂式建築為基礎，舊時用以突顯圖書館所在地「知識堡壘」之意涵。文化大學郵局亦設於此處。","align":"center","wrap":True},{"type":"button","action":{"type":"message","label":"往孔子大道","text":"孔子大道02"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"現在有15人在這裡","align":"center"},{"type":"button","action":{"type":"message","label":"留言板","text":"百花池廣場留言板"},"gravity":"center"}]}})
		)	
		positionCodename[-1] = 1
		return True
	else:
		return False

def position_DaAn(event):
	if '大恩館' in event.message.text:
		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(alt_text='porn template', contents = {"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"大恩館","align":"center"}]},"hero":{"type":"image","url":"https://pic.pimg.tw/b03050ia/1542459189-3300981281_n.jpg","size":"full","aspectRatio":"1.51:1","aspectMode":"fit"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"別名華僑塔，又名「開國紀念館」，許多辦公室都在此處，需要辦理事情的話都會來這邊。","align":"center","wrap":True},{"type":"button","action":{"type":"message","label":"往大功館","text":"大功館"}},{"type":"button","action":{"type":"message","label":"往孔子大道","text":"孔子大道01"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"現在有15人在這裡","align":"center"},{"type":"button","action":{"type":"message","label":"留言板","text":"百花池廣場留言板"},"gravity":"center"}]}})
		)	
		positionCodename[-1] = 1
		return True
	else:
		return False

def position_DaGon(event):
	if '大功館' in event.message.text:
		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(alt_text='porn template', contents = {"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"大功館","align":"center"}]},"hero":{"type":"image","url":"https://b.share.photo.xuite.net/youngbirdpapago/1b38ff4/9649470/422937014_m.jpg","size":"full","aspectRatio":"1.51:1","aspectMode":"fit"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"為農學院所在，由該校建築暨都市設計系前任系主任徐秀夫教授設計。","align":"center","wrap":True},{"type":"button","action":{"type":"message","label":"往大恩館","text":"大恩館"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"現在有15人在這裡","align":"center"},{"type":"button","action":{"type":"message","label":"留言板","text":"百花池廣場留言板"},"gravity":"center"}]}})
		)	
		positionCodename[-1] = 1
		return True
	else:
		return False


def position_DaRenCourt(event):
	if '大仁球場' in event.message.text:
		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(alt_text='porn template', contents = {"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"大仁球場","align":"center"}]},"hero":{"type":"image","url":"https://pic.pimg.tw/springsun0410/1411883079-2925202155_n.jpg","size":"full","aspectRatio":"1.51:1","aspectMode":"fit"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"許多人在旁邊圍觀、聊天、加油打氣，許多校內比賽都會在旁邊的球場上進行。","align":"center","wrap":True},{"type":"button","action":{"type":"message","label":"往基督大道","text":"基督大道02"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"現在有15人在這裡","align":"center"},{"type":"button","action":{"type":"message","label":"留言板","text":"百花池廣場留言板"},"gravity":"center"}]}})
		)	
		positionCodename[-1] = 1
		return True
	else:
		return False


def positionCheck(event):
	print('呼叫位置', positionCodename[-1])
	if '位置' in event.message.text:

		if (positionCodename[-1] == 1):
			line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text="歡迎來到百花池")
		)
		elif (positionCodename[-1] == 2):
			line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text="歡迎來到大義館")
		)
		elif (positionCodename[-1] == 3):
			line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text="歡迎來到大仁館")
		)
		return True

	else:
		return False



