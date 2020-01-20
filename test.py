import requests
import json
import firebase_admin
from firebase_admin import credentials, firestore

defaultURL = 'https://www.thebluealliance.com/api/v3'
askFotTeamsInDe1 =  '/event/'
eventKey = u'2020isde'
header = 'X-TBA-Auth-Key'
headerKey = 'ptM95D6SCcHO95D97GLFStGb4cWyxtBKNOI9FX5QmBirDnjebphZAEpPcwXNr4vH'


num = raw_input('enter ditrict number \n')
askFotTeamsInDe1 = askFotTeamsInDe1 + eventKey + str(num) + "/teams"
# askFotTeamsInDe1 = askFotTeamsInDe1 + eventKey + str(num) + "/matches/simple"
cred = credentials.Certificate('./ServiceAccountKey.json',)
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
#
response = requests.get(defaultURL + askFotTeamsInDe1, headers = {header: headerKey})
json_obj = json.loads(response.content)

def uploadScoutresTaskes():
    listOfUsers = [u'1C3f85SNrDMOZVTkssdXdd7NkVV2', u'Odi2opRmUHbhXuw3pbNIVqN5opp1', u'KuafUEj5Maa1CkVikFSLV5NNI2L2']

    for m in range(len(listOfUsers)):
        db.collection(u'users').document(listOfUsers[m]) \
            .collection(u'tournaments').document(u'ISRD' + str(num)).set({
        })

        for i in range(len(json_obj)):
            if str(json_obj[i][u'comp_level']) == (u'qm'):
                match_number = json_obj[i][u'match_number']
                teamToScout = str(json_obj[i][u'alliances'][u'red'][u'team_keys'][m]).split(u'frc')
                db.collection(u'users').document(listOfUsers[m]) \
                    .collection(u'tournaments').document(u'ISRD' + str(num)).collection(u'gamesToScout') \
                    .document(str(match_number)).set({
                    u'teamNumber': teamToScout[1],
                    u'saved': False
                })

print json_obj
listD1 = []
for i in range(len(json_obj)):
    print json_obj[i]["team_number"]
    listD1.append(json_obj[i]["team_number"])

eventKey = u'2020isde'
num = raw_input('enter ditrict number \n')
askFotTeamsInDe1 =  '/event/'
defaultURL = 'https://www.thebluealliance.com/api/v3'
askFotTeamsInDe1 = askFotTeamsInDe1 + eventKey + str(num) + "/teams"
print askFotTeamsInDe1
# askFotTeamsInDe1 = askFotTeamsInDe1 + eventKey + str(num) + "/matches/simple"
#
# print defaultURL + askFotTeamsInDe1
# response = requests.get(defaultURL + askFotTeamsInDe1, headers = {header: headerKey})
# json_obj = json.loads(response.content)
#
# listD3 = []
# for i in range(len(json_obj)):
#     print json_obj[i]["team_number"]
#     listD3.append(json_obj[i]["team_number"])
#
# finalList =[]
# for i in range(len(listD1)):
#     print listD1[i]
#     for m in range(len(listD3)):
#         if listD3[m]==listD1[i]:
#             finalList.append(listD1[i])
#
# print finalList
#
# finalfinal = []
# for i in range(len(finalList)):
#     print 1
#     defaultURL = 'https://www.thebluealliance.com/api/v3'
#     askFotTeamsInDe1 = '/team/'
#     eventKey = u'frc' + str(finalList[i])
#     askFotTeamsInDe2 = '/awards'
#     askFotTeamsInDe1 = askFotTeamsInDe1 + str(eventKey) + askFotTeamsInDe2
#     print defaultURL + askFotTeamsInDe1
#     response = requests.get(defaultURL + askFotTeamsInDe1, headers={header: headerKey})
#     json_obj = json.loads(response.content)
#     print response
#     print json_obj
#     count = 0;
#     for m in range(len(json_obj)):
#         if json_obj[m][u'award_type'] == 1:
#             count = count + 1
#     if count>5:
#         finalfinal.append(finalList[i])
# print finalfinal

# collection(u'gamesToScout').document(x)

# for i in range(len(json_obj)):
#     team_number = json_obj[i]["team_number"]
#     team_name = json_obj[i]["nickname"]
#
#     db.collection(u'tournaments').document(u'ISRD' + str(num)).collection(u'teams').document(str(team_number)).set({
#         u'team_name': team_name,
#         u'pit_scouting_saved': False
#     })
#     db.collection(u'tournaments').document(u'ISRD'  + str(num)).collection(u'teams').document(str(team_number)).collection(u'superScouting')
#     db.collection(u'tournaments').document(u'ISRD' + str(num)).collection(u'teams').document(str(team_number)).collection(u'scouting')
#
#
#
#     # print str(team_number) + ' - ' + str(team_name)
#
#
#     # db.collection(u'tournaments').document(u'ISRD'  + str(num)).collection(u'teams').document(str(team_number)).collection(
#     #     u'scoutingData').document(u'pitScouting').set({
#     #     # u'saved': False,
#     #     # u'Robot Weight': 0,
#     #     # u'Robot Width': 0,
#     #     # u'Robot Length': 0,
#     #     # u'DT Motors': 0
#     # })
#     # (u'scoutingData').collection
#     # db.collection(u'teams').document(str(team_number)).collection(u'pitScouting').document(u'test').set({
#     #     u'test':team_number
#     # })
#     # db.collection(u'teams').document(str(team_number)).collection(u'superScouting').document(u'test').set({
#     #     u'test': team_number
#     # })



# def teamsInQualList(json_obj, keyList):
#     FinalTeamList = []
#     for i in range(len(json_obj)):
#         for m in range(len(keyList)):
#             if str(json_obj[i]["key"]) == str(keyList[m]):
#                 FinalTeamList.append(str(json_obj[i]["team_number"]) + " - " + str(json_obj[i]["nickname"]))
#     return FinalTeamList;
#
# alliances = json_obj["alliances"]
# blue = alliances["blue"]
# red = alliances["red"]
# blueTeams = blue["team_keys"]
# redTeams = red["team_keys"]
# blueTeamsKeyList =[]
# redTeamsKeyList =[]
# for i in range(len(blueTeams)):
#     blueTeamsKeyList.append(blueTeams[i])
# for i in range(len(redTeams)):
#     redTeamsKeyList.append(redTeams[i])
# askFotTeamsInDe1 = '/event/2019iscmp/teams'
# response = requests.get(defaultURL + askFotTeamsInDe1, headers = {header: headerKey})
#
# json_obj = json.loads(response.content)
#
# print teamsInQualList(json_obj, blueTeamsKeyList)
# print teamsInQualList(json_obj, redTeamsKeyList)
