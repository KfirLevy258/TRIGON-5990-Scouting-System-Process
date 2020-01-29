import firebase_admin
from firebase_admin import credentials, firestore
import requests
import json

eventKey = u'2019isde'
# eventKey = u'2019iscmp'

def get_api_data(num):
    defaultURL = 'https://www.thebluealliance.com/api/v3'
    askFotTeamsInDe1 = '/event/'
    header = 'X-TBA-Auth-Key'
    headerKey = 'ptM95D6SCcHO95D97GLFStGb4cWyxtBKNOI9FX5QmBirDnjebphZAEpPcwXNr4vH'

    if (eventKey == u'2019iscmp'):
        askFotTeamsInDe1 = askFotTeamsInDe1 + eventKey + "/teams"
    else :
        askFotTeamsInDe1 = askFotTeamsInDe1 + eventKey + str(num) + "/teams"

    print defaultURL + askFotTeamsInDe1
    response = requests.get(defaultURL + askFotTeamsInDe1, headers={header: headerKey})
    json_obj = json.loads(response.content)
    return json_obj

cred = credentials.Certificate('./ServiceAccountKey.json',)
default_app = firebase_admin.initialize_app(cred)
database = firestore.client()

num = raw_input('enter ditrict number \n')
json_obj = get_api_data(num)

database.collection(u'tournaments').document(u'ISRD' + str(num)).set({
    u'event_key': eventKey + num
})

for i in range(len(json_obj)):
    team_number = json_obj[i]["team_number"]
    team_name = json_obj[i]["nickname"]

    database.collection(u'tournaments').document(u'ISRD' + str(num)).collection(u'teams').document(str(team_number)).set({
        u'team_name': team_name,
        u'pit_scouting_saved': False
    })
    database.collection(u'tournaments').document(u'ISRD'  + str(num)).collection(u'teams').document(str(team_number)).collection(u'superScouting')
    database.collection(u'tournaments').document(u'ISRD' + str(num)).collection(u'teams').document(str(team_number)).collection(u'scouting')

