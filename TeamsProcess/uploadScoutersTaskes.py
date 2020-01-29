import firebase_admin
from firebase_admin import credentials, firestore
import requests
import json

eventKey = u'2019isde'

def get_api_data(num):
    defaultURL = 'https://www.thebluealliance.com/api/v3'
    askFotTeamsInDe1 = '/event/'
    header = 'X-TBA-Auth-Key'
    headerKey = 'ptM95D6SCcHO95D97GLFStGb4cWyxtBKNOI9FX5QmBirDnjebphZAEpPcwXNr4vH'

    askFotTeamsInDe1 = askFotTeamsInDe1 + eventKey + str(num) + "/matches/simple"

    response = requests.get(defaultURL + askFotTeamsInDe1, headers={header: headerKey})
    json_obj = json.loads(response.content)
    return json_obj

cred = credentials.Certificate('./ServiceAccountKey.json',)
default_app = firebase_admin.initialize_app(cred)
database = firestore.client()

num = raw_input('enter ditrict number \n')
json_obj = get_api_data(num)

listOfUsers = [u'1C3f85SNrDMOZVTkssdXdd7NkVV2', u'Odi2opRmUHbhXuw3pbNIVqN5opp1', u'KuafUEj5Maa1CkVikFSLV5NNI2L2']
for m in range(len(listOfUsers)):
    database.collection(u'users').document(listOfUsers[m]) \
    .collection(u'tournaments').document(u'ISRD' + str(num)).set({

    })
    for i in range(len(json_obj)):
        if str(json_obj[i][u'comp_level']) == (u'qm'):
             match_number = json_obj[i][u'match_number']
             teamToScout = str(json_obj[i][u'alliances'][u'red'][u'team_keys'][m]).split(u'frc')
             database.collection(u'users').document(listOfUsers[m]) \
                        .collection(u'tournaments').document(u'ISRD' + str(num)).collection(u'gamesToScout') \
                        .document(str(match_number)).set({
             u'teamNumber': teamToScout[1],
             u'saved': False,
             u'allianceColor': u'red'
        })
