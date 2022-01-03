from get_most_recent_tweets import get_user_id
import json

input_dict = {"CHANNEL_ID": 123456789101112131, # change your channel ID here
              "MINUTE_INTERVAL": 5, # change to the minute interval that you want 
              "NSWHealth": ["covid-19", "update"], # change to the twitter accounts and keywords that you want to follow
              "VicGovDH": ["#covid19data", "new", "cases"],
              "SAHealth": ["covid-19", "update"],
              "ACTHealth": ["new", "cases"],
              "qldhealth": ["new", "cases"]}

id_dict = {}
for key in input_dict:
    if key in ['CHANNEL_ID', 'MINUTE_INTERVAL']:
        id_dict[key] = input_dict[key]
    else:
        user_id = get_user_id(key)
        id_dict[key] = [user_id, input_dict[key]]

with open('./ids.json', 'w+') as f:
    json.dump(id_dict, f)
