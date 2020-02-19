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

# json = get_api_data(district_number, "/matches/simple")
# json_obj = get_api_data(district_number, "/teams")
# teamList = get_teams_list(json_obj)
#
# print (len(teamList) / float(get_users_amount())) # teams for each scouter

scouters = get_users_list()
print scouters
json = get_api_data(district_number, "/matches/simple")
matches = get_quals_data(json)

# firstShift = True
# for i in range(len(matches)):
#     for m in range(len(scouters/2)):
#         if firstShift:
#             print
# for m in range(len(listOfUsersBlue)):
#
#
#
#     for k in range(len(listOfUsersBlue[m])):
#         # database.collection(u'users').document(listOfUsersRed[m][i]) \
#         #     .collection(u'tournaments').document(u'ISRD' + str(districtNumber)).set({
#         #
#         # })
#         database.collection(u'users').document(listOfUsersBlue[m][k]) \
#             .collection(u'tournaments').document(u'PreSeason').set({
#
#         })
#
#         for i in range(len(json)):
#             if str(json[i][u'comp_level']) == (u'qm'):
#                 match_number = str(json[i][u'match_number'])
#                 if int(match_number) < 10:
#                     match_number = u'0' + str(match_number)
#                 teamToScout = str(json[i][u'alliances'][u'blue'][u'team_keys'][m]).split(u'frc')
#                 database.collection(u'users').document(listOfUsersBlue[m][k]) \
#                     .collection(u'tournaments').document(u'PreSeason').collection(u'gamesToScout') \
#                     .document(str(match_number)).set({
#                     u'teamNumber': teamToScout[1],
#                     u'saved': False,
#                     u'allianceColor': u'blue'
#                 })

#
# listOfUsersRed = [[u'5Aevkki6QpRN0xChGv3xTfnA4h32', u'DQ7F7tXIoLVJeqWmnYlzPFBO0Xw2', u'G2d1Lb83TDQgqoVhSV3i9I9yVTN2'],
#                   [u'J5xfo4x0SIToqKYX8rG9IbhQScJ3', u'K6nH9JzzrobSg0vhxC6a8Hk0pIG3', u'KuafUEj5Maa1CkVikFSLV5NNI2L2'],
#                   [u'NyBLGLTeQzXVPnc09qqnuywq9iy2', u'PbokaHDPzHdqvd323o7JMw5bETF2', u'VUXysa3cnGeuIqTRWRCbsgljX062']]
# listOfUsersBlue = [[u'YH7wXhrgkgM2ZeVwqoQ4kH1C87o1', u'bZtYnZv7IOUe9s6xXQ8eG74CsUr1', u'dOC7jFDcyPNtsVpRoqb3vm4QssJ2'],
#                   [u'gJWkTZD9adZclSGez0Lw6ms4d3w2', u'ilk7QtgVjuR3VF35RWYiLTNex853', u'q6kLtZncQZcOgWQ2T9zRIUECqFk1'],
#                   [u'vui79lCDT5NtzI4uGNb9M0N6q983', u'wIXqPpF1tlbbBmsnHElCn8lEgwm2', u'yESKrNoKcNZYOZ7cjFgbfcJ8QvL2']]

# for m in range(len(listOfUsersRed)):
#     for k in range(len(listOfUsersRed[m])):
#         # database.collection(u'users').document(listOfUsersRed[m][i]) \
#         #     .collection(u'tournaments').document(u'ISRD' + str(districtNumber)).set({
#         #
#         # })
#         database.collection(u'users').document(listOfUsersRed[m][k]) \
#             .collection(u'tournaments').document(u'PreSeason').set({
#
#         })
#
#         for i in range(len(json)):
#             if str(json[i][u'comp_level']) == (u'qm'):
#                 match_number = str(json[i][u'match_number'])
#                 if int(match_number) < 10:
#                     match_number = u'0' + str(match_number)
#                 teamToScout = str(json[i][u'alliances'][u'red'][u'team_keys'][m]).split(u'frc')
#                 database.collection(u'users').document(listOfUsersRed[m][k]) \
#                     .collection(u'tournaments').document(u'PreSeason').collection(u'gamesToScout') \
#                     .document(str(match_number)).set({
#                     u'teamNumber': teamToScout[1],
#                     u'saved': False,
#                     u'allianceColor': u'red'
#                 })