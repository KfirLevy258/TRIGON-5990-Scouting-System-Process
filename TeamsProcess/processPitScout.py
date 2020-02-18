import firebase_admin
from firebase_admin import credentials, firestore
import requests
import json

def get_chassis_overall_strength(team_data):
    wheelDiameter = team_data.get(u'Pit_scouting').get(u'Chassis Overall Strength').get(u'Wheel Diameter')
    DTMotorType = team_data.get(u'Pit_scouting').get(u'Chassis Overall Strength').get(u'DT Motor type')
    conversionRatio = team_data.get(u'Pit_scouting').get(u'Chassis Overall Strength').get(u'Conversion Ratio')
    conversionRatio = str(conversionRatio).split(u'/')
    conversionRatio = float(conversionRatio[0])/float(conversionRatio[1])
    # to do - return real value
    print wheelDiameter
    print conversionRatio
    return DTMotorType

def get_api_data(num):
    defaultURL = 'https://www.thebluealliance.com/api/v3'
    askFotTeamsInDe1 = '/event/'
    eventKey = u'2019isde'
    header = 'X-TBA-Auth-Key'
    headerKey = 'ptM95D6SCcHO95D97GLFStGb4cWyxtBKNOI9FX5QmBirDnjebphZAEpPcwXNr4vH'

    askFotTeamsInDe1 = askFotTeamsInDe1 + eventKey + str(num) + "/teams"

    response = requests.get(defaultURL + askFotTeamsInDe1, headers={header: headerKey})
    json_obj = json.loads(response.content)
    return json_obj

cred = credentials.Certificate('./ServiceAccountKey.json',)
default_app = firebase_admin.initialize_app(cred)
database = firestore.client()

# teamNumber = raw_input('Enter team number: ')
# districtNumber = raw_input('Enter district number: ')
districtNumber = 3
teamNumber = 1574

teamData = database.collection(u'tournaments').document(u'ISRD' + str(districtNumber)).collection(u'teams')\
    .document(str(teamNumber)).get()


# get_chassis_overall_strength(teamData)

num = raw_input('enter ditrict number \n')
json_obj = get_api_data(num)

database.collection(u'tournaments').document(u'ISRD' + str(num)).set({
    u'event_key': u'2019isde' + num
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

