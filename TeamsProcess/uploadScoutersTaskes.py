import firebase_admin
from firebase_admin import credentials, firestore
import requests
import json

eventKey = u'2019isde'

def get_api_data(districtNumber, requestKind):
    defaultURL = 'https://www.thebluealliance.com/api/v3'
    askFotTeamsInDe1 = '/event/'
    header = 'X-TBA-Auth-Key'
    headerKey = 'ptM95D6SCcHO95D97GLFStGb4cWyxtBKNOI9FX5QmBirDnjebphZAEpPcwXNr4vH'

    askFotTeamsInDe1 = askFotTeamsInDe1 + eventKey + str(districtNumber) + requestKind

    response = requests.get(defaultURL + askFotTeamsInDe1, headers={header: headerKey})
    print(defaultURL + askFotTeamsInDe1)
    jsonResponse = json.loads(response.content)
    return jsonResponse

def get_teams_list(listToGetFrom):
    teamsList = []
    for counter in range(len(listToGetFrom)):
        teamsList.append(listToGetFrom[counter][u'team_number'])
    return teamsList

def get_users_list():
    listOfUsers = []
    scouters = database.collection(u'users').where(u'activeScouter', u'==', True).stream()
    for scouter in scouters:
        listOfUsers.append(scouter.to_dict())
    return listOfUsers

def get_quals_data(listToGetFrom):
    listOfQuals = []
    for counter in range(len(listToGetFrom)):
        if str(json[counter][u'comp_level']) == (u'qm'):
            listOfQuals.append(Match(json[counter]))
    return listOfQuals

def upload_task(userId, district, teamNumber, allianceColor, matchNumber):
    if int(matchNumber) < 10:
        matchNumber = u'0' + str(matchNumber)
    database.collection(u'users').document(userId) \
            .collection(u'tournaments').document(district).set({})
    database.collection(u'users').document(userId) \
            .collection(u'tournaments').document(district).collection(u'gamesToScout').\
                document(str(matchNumber)).set({
        u'allianceColor': allianceColor,
        u'saved': False,
        u'teamNumber': teamNumber
    })

class Match:
    matchNumber = 0
    teamsInQual = []

    def __init__(self, json):
        self.teamsInQual = []
        self.matchNumber = json[u'match_number']
        for i in range(len(json[u'alliances'][u'blue'][u'team_keys'])):
            self.teamsInQual.append(
                {u'teamNumber': str(json[u'alliances'][u'blue'][u'team_keys'][i]).split(u'frc')[1],
                 u'allianceColor': u'blue'})
        for i in range(len(json[u'alliances'][u'red'][u'team_keys'])):
            self.teamsInQual.append(
                {u'teamNumber': str(json[u'alliances'][u'red'][u'team_keys'][i]).split(u'frc')[1],
                 u'allianceColor': u'red'})

restTime = 5
cred = credentials.Certificate('./ServiceAccountKey.json', )
default_app = firebase_admin.initialize_app(cred)
database = firestore.client()

district_number = raw_input('enter ditrict number \n')

#
#
# print (len(teamList) / float(get_users_amount())) # teams for each scouter

scouters = get_users_list()
json = get_api_data(district_number, "/matches/simple")
matches = get_quals_data(json)
matches.sort(key=lambda x: x.matchNumber)

firstShiftList = scouters[:(len(scouters)/2)]
secondShiftList = scouters[(len(scouters)/2):]

firstShift = False
for i in range(len(matches)):
    if (i % restTime == 0):
        firstShift = not firstShift
        print str(i) + u' matches loaded'
    if firstShift:
        for m in range(len(firstShiftList)):
            upload_task(firstShiftList[m][u'uid'], u'ISRD' + district_number, matches[i].teamsInQual[m][u'teamNumber'],
                        matches[i].teamsInQual[m][u'allianceColor'], matches[i].matchNumber)
    else:
        for m in range(len(secondShiftList)):
            upload_task(secondShiftList[m][u'uid'], u'ISRD' + district_number, matches[i].teamsInQual[m][u'teamNumber'],
                        matches[i].teamsInQual[m][u'allianceColor'], matches[i].matchNumber)
print u'all matches loaded (' + str(len(matches)) + u'matches)'

# json_obj = get_api_data(district_number, "/teams")
# teamList = get_teams_list(json_obj)
# for i in range(len(teamList)):
#