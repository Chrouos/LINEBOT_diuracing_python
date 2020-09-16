from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import FlexSendMessage

import re
from custom_models import utils

# LINE 聊天機器人的基本資料:
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


# whatDoYouWanToMove
whatDoYouWanToMove = {"type":"bubble","body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"您目前的位置是","align":"center"},{"type":"text","text":"請問你要怎麼操作","weight":"bold","size":"xl","align":"center"}]},"footer":{"type":"box","layout":"vertical","spacing":"sm","contents":[{"type":"button","style":"link","height":"sm","action":{"type":"uri","label":"上","uri":"https://linecorp.com"}},{"type":"button","style":"link","height":"sm","action":{"type":"uri","label":"下","uri":"https://linecorp.com"}},{"type":"button","action":{"type":"uri","label":"左","uri":"http://linecorp.com/"}},{"type":"button","action":{"type":"uri","label":"右","uri":"http://linecorp.com/"}}],"flex":0}}


