import psycopg2
import os

# 使用者創建帳號密碼，存入資料 (INSERT)
def line_insert_record(record_list):
	print(record_list)
	DATABASE_URL = os.environ['DATABASE_URL']
	
	conn = psycopg2.connect(DATABASE_URL, sslmode='require')
	cursor = conn.cursor()

	cursor.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'diuracing_table_people'")

	table_columns = '(user_id, username, password, date, position_x, position_y, position_z)'
	postgres_insert_query = f"""INSERT INTO diuracing_table_people {table_columns} VALUES (%s, %s, %s, %s, %s, %s, %s);"""

	cursor.executemany(postgres_insert_query, record_list)
	conn.commit()
	
	message = f"恭喜您，玩家！ 歡迎加入我們！"
	print(message)
	
	cursor.close()
	conn.close()

	return message

# 查詢目前所在位置
def line_select_overall(text):
	print('line_select_overall')
	DATABASE_URL = os.environ['DATABASE_URL']

	conn = psycopg2.connect(DATABASE_URL, sslmode='require')
	cursor = conn.cursor()

	tempUsernameList = text.split()
	tempUsernameList.remove('位置')

	tempUsername = tempUsernameList[0]

	postgres_select_query = f"""SELECT position_x, position_y, position_z FROM diuracing_table_people WHERE username = 'diudiu' """   
	cursor.execute(postgres_select_query)
	
	raw = cursor.fetchmany(1) # 一筆一筆資料放進LIST回傳

	temp = []
	for i in range(3):
		temp.append(raw[0][i])
		
	print(temp)
	message = 'X座標： {0} , Y座標： {1} , 第 {2} 樓'.format(temp[0], temp[1], temp[2])
	
	cursor.close()
	conn.close()
	
	return message