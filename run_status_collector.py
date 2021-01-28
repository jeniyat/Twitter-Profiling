# import sys
# import codecs
# import commands
# reload(sys)
# sys.setdefaultencoding( "utf-8" )


#from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import json
import tweepy
import twitter
import csv
import os


class TIMELINE_EXTRACTOR:
	
	def __init__(self, op_dir):
		
		self.output_directory=op_dir
		self.list_of_user_ids={}
		self.prev_extracted_users=set()

		#-----------ashutosh's tokens-----------------------
		CONSUMER_KEY = 'xxxxxxxx'
		CONSUMER_SECRET = 'xxxxxxxx'
		ACCESS_TOKEN = 'xxxxxxxx'
		ACCESS_SECRET = 'xxxxxxxx'


		self.api = twitter.Api(consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET,access_token_key=ACCESS_TOKEN,access_token_secret=ACCESS_SECRET,sleep_on_rate_limit=True)

	
	def read_ip_files(self,list_of_ip_files):
		for ip_file in list_of_ip_files:
			for line in open(ip_file):
				
				user_id=str(line.strip())
				self.list_of_user_ids[user_id]=int(user_id)

		print("Sanity Check: ",len(self.list_of_user_ids.keys()))

	def read_and_write_status(self,user_id,error_file):
		op_file_name_all =self.output_directory+str(user_id)+".json"
		if os.path.exists(op_file_name_all):
			print("file exists")
			return
		try:
			status = self.api.GetUserTimeline(user_id=user_id, count=200)
			#status = self.api.user_timeline(user_id=user_id, count=200,tweet_mode='extended')
		except Exception as e:
			ferr=open(error_file,'a')
			print(self.list_of_user_ids[str(user_id)])
			op_dict={}
			op_dict["user_id"]=user_id
			# op_dict["user_id_h"]=self.list_of_user_ids[str(user_id)]["user_id_h"]
			op_dict["timeline_error"]=str(e)
			error_str= json.dumps(op_dict)+"\n"
			ferr.write(error_str)
			ferr.close()
			print("DBUG----: error in read_and_write_status: ",e)
			return


		op_file_name_all =self.output_directory+str(user_id)+".json"
		Fout_all= open(op_file_name_all,"w")

		

		for item in status:
			str_item = str(item)
			json_obj = json.loads(str_item)
			Fout_all.write(json.dumps(json_obj))
			#Fout_all.write(json.dumps(item))
			Fout_all.write("\n")

		Fout_all.close()

	def extract_status(self, error_file):
		ferr=open(error_file,'a')
		ferr.close()
		count=0
		for user_id in self.list_of_user_ids:
			print(self.list_of_user_ids[user_id])
			#print(type(user_id)), user_id
			try:
				u_id = int(user_id)
				self.read_and_write_status(u_id,error_file)
				#if count==5: break
				print("Progress Check: ",count)
				
			except Exception as e:
				#print op_dict
				print("DBUG----: error in run_status_collection: ",e)
				continue
			count+=1

		
		
if __name__ == '__main__':
	status_op_directory="status_json_all/"
	error_file_name="status_error_all.json"

	list_of_input_files=["CP3_airstrikes_userIDs_botometer_humanizer","CP3_whitehelmets_userIDs_botometer_humanizer"]

	try:
		os.stat(status_op_directory)
	except:
		os.mkdir(status_op_directory)

	timeline_extractor=TIMELINE_EXTRACTOR(status_op_directory)

	
	timeline_extractor.read_ip_files(list_of_input_files)

	timeline_extractor.extract_status(error_file_name)

	





