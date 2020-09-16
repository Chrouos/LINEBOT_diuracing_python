from __future__ import unicode_literals

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage

import configparser

from apscheduler.schedulers.blocking import BlockingScheduler
import urllib
import datetime

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

# CLOCK
sched = BlockingScheduler()

# 每兩分鐘叫醒一次HEROKU
@sched.scheduled_job('cron', minute='*/2')
def scheduled_job():
    print('========== APScheduler CRON =========')
    # 馬上讓我們瞧瞧
    print('This job runs every day */2 min.')
    # 利用datetime查詢時間
    print(f'{datetime.datetime.now().ctime()}')
    print('========== APScheduler CRON =========')

    url = "https://diuracing.herokuapp.com/"
    conn = urllib.request.urlopen(url)
        
    for key, value in conn.getheaders():
        print(key, value)



@sched.scheduled_job('cron', day_of_week='sun', hour=6, minute=0)
def scheduled_job():
    print('========== APScheduler CRON =========')
    print('This job is run every weekday at 6:30')
    print('========== APScheduler CRON =========')

    # 禮拜日 早上六點零分時，會自動傳送訊息(鬧鐘，確認功能正常)
    line_bot_api.push_message('Uf2b87f0a26b55b74b06b54b826469d24', TextSendMessage(text='Good Morning!'))

sched.start()