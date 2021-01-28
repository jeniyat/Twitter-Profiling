import botometer
import random
import json
import csv
import time
import datetime

class BOTOMETER:
	
	def __init__(self):
		
		mashape_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
		
		
		CONSUMER_KEY = 'xxxxxxxx'
		CONSUMER_SECRET = 'xxxxxxxx'
		ACCESS_TOKEN = 'xxxxxxxx'
		ACCESS_SECRET = 'xxxxxxxx'

		twitter_app_auth = {
		    'consumer_key': CONSUMER_KEY,
		    'consumer_secret': CONSUMER_SECRET,
		    'access_token': ACCESS_TOKEN,
		    'access_token_secret': ACCESS_SECRET,
		}

		self.bom = botometer.Botometer(wait_on_ratelimit=True,
		                          mashape_key=mashape_key,
		                          **twitter_app_auth)

		self.list_of_user_ids=set()



	

	def read_ip_file(self, input_file):
		
		for row in open(input_file):
			print(row)
			user_id=int(row.strip())
			self.list_of_user_ids.add(user_id)

	def collect_user_ids(self,list_of_csv_file):
		for csv_file in list_of_csv_file:
			self.read_ip_file(csv_file)
		
		

	

	def run_botometer_score_collection(self,op_file_name, error_file_name, limit_per_day):
		fout=open(op_file_name,'w')
		ferr=open(error_file_name,'w')
		count=0

		api_count=0
		for user_id in self.list_of_user_ids:
			try:
				#print(user_id)
				#print("Progress Check: ",count)
				result = self.bom.check_account(user_id)
				result_str= json.dumps(result)+"\n"
				fout.write(result_str)
				fout.flush()
				print("Progress Check: ",count)
				#if count==5:break
				if api_count==limit_per_day:
					tomorrow = datetime.datetime.replace(datetime.datetime.now() + datetime.timedelta(days=1), hour=0, minute=0, second=0)
					delta = tomorrow - datetime.datetime.now()
					time.sleep(delta.seconds)
					api_count=0
			except Exception as e:
				err_dict={}
				err_dict["error"]=str(e)
				err_dict["user_id"]=user_id
				err_str= json.dumps(err_dict)+"\n"
				ferr.write(err_str)
				ferr.flush()
				print("DBUG----: error in run_botometer_score_collection: ",e)
				continue
			count+=1
			api_count+=1
		fout.close()
		ferr.close()

		
		


if __name__ == '__main__':
	botometer= BOTOMETER()

	list_of_input_files=["CP3_airstrikes_userIDs_botometer_humanizer","CP3_whitehelmets_userIDs_botometer_humanizer"]

	botometer.collect_user_ids(list_of_input_files)
	print("Sanity Check: ",len(botometer.list_of_user_ids))

	op_file_name="botometer_score.json"
	error_file_name="botometer_error_all.json"
	limit_per_day=17280
	botometer. run_botometer_score_collection(op_file_name, error_file_name, limit_per_day)






