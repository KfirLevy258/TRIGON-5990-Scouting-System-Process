import requests
import json

#response = requests.get('https://www.thebluealliance.com/api/v3/team/frc5990?X-TBA-Auth-Key=ptM95D6SCcHO95D97GLFStGb4cWyxtBKNOI9FX5QmBirDnjebphZAEpPcwXNr4vH')
response = requests.get('https://www.thebluealliance.com/api/v3/team/frc5990', headers = {'X-TBA-Auth-Key': 'ptM95D6SCcHO95D97GLFStGb4cWyxtBKNOI9FX5QmBirDnjebphZAEpPcwXNr4vH'})
#string = response.read().decode('utf-8')
json_obj = json.loads(response.content)

print(json_obj['city']) # prints the string with 'source_name' key
