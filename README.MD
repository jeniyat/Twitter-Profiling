1. Extacting botometer score:
	This process is done using the botometer-python library: https://github.com/IUNetSci/botometer-python
	Here we have also attached a sample scirpt run_botometer.py to extract botometer scores from a list of user_ids.
	Changes needed to make in this script:
	-- please use a valid mashup key. mashup keys can be get from: https://rapidapi.com/OSoMe/api/botometer?utm_source=mashape&utm_medium=301
	-- please use valid twitter tokens [CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET]
	-- please update the list of input files in if __name__ == '__main__':

	Command to run: python2.7 run_botometer.py

	Output_1: botometer_score.json. This file will contain the botometer scores for all user id
	Output_2: botometer_error_all.json. This file will contain errors for the user ids that botometer was not able to extract.

2. Extracting humanizr: 
	
	Step 1: First we need to extract a folder with status from users.
	To do that we need to use the script: run_status_collector.py
	
	Changes needed to make in this script:
	-- please use valid twitter tokens [CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET]
	-- please update the list of input files in if __name__ == '__main__':

	Command to run: python2.7 run_status_collector.py

	Output_1: status_json_all/. This folder will contain the status in json formmat for all user id
	Output_2: status_error_all.json. This file will contain errors for the user ids that the status collector was not able to extract.

	Step 2: In the second step we will extract humanizr score using hte github repository: https://github.com/Humanizr/Humanizer. Please clone the repository and install the package by following the instruction in the repository.

	After cloning the repository, you can run the run_humanizr.sh script to extract the humanizr output: 
	Changes needed to make in this script:
	-- Please update the DIR with the location of the cloned humanizr directory 
	-- Please update the TWEET_DIR with the status folder found using Step 1

	Command to run: bash run_humanizr.sh

	Output_1: humanizr.tsv. This file will contain the humanizr output for all user id











