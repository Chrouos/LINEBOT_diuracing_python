import datetime

# 使用者創建帳號密碼，弄成LIST
def prepare_record(text, user_id): 

	record_list= []
	
	text_list = text.split()
	text_list.remove('創建角色:')
	text_list.append(str(datetime.date.today()))

	temp_user_id = user_id
	temp_username = text_list[0]
	temp_password = text_list[1]
	temp_date = text_list[2]
	

	record = (temp_user_id, temp_username, temp_password, temp_date, int(0), int(0), int(1))
	record_list.append(record)
	
	return record_list

