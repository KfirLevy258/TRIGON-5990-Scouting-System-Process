import firebase_admin
from firebase_admin import credentials, firestore
import requests
import json

# eventKey = u'2019isde'
eventKey = u'2020week0'


def get_api_data(num):
    defaultURL = 'https://www.thebluealliance.com/api/v3'
    askFotTeamsInDe1 = '/event/'
    header = 'X-TBA-Auth-Key'
    headerKey = 'ptM95D6SCcHO95D97GLFStGb4cWyxtBKNOI9FX5QmBirDnjebphZAEpPcwXNr4vH'

    # askFotTeamsInDe1 = askFotTeamsInDe1 + eventKey + str(num) + "/matches/simple"
    askFotTeamsInDe1 = askFotTeamsInDe1 + eventKey + "/matches/simple"

    response = requests.get(defaultURL + askFotTeamsInDe1, headers={header: headerKey})
    print(defaultURL + askFotTeamsInDe1)
    json_obj = json.loads(response.content)
    return json_obj


cred = credentials.Certificate('./ServiceAccountKey.json', )
default_app = firebase_admin.initialize_app(cred)
database = firestore.client()

num = raw_input('enter ditrict number \n')
json_obj = get_api_data(num)

listOfUsersRed = [[u'5Aevkki6QpRN0xChGv3xTfnA4h32', u'DQ7F7tXIoLVJeqWmnYlzPFBO0Xw2', u'G2d1Lb83TDQgqoVhSV3i9I9yVTN2'],
                  [u'J5xfo4x0SIToqKYX8rG9IbhQScJ3', u'K6nH9JzzrobSg0vhxC6a8Hk0pIG3', u'KuafUEj5Maa1CkVikFSLV5NNI2L2'],
                  [u'NyBLGLTeQzXVPnc09qqnuywq9iy2', u'PbokaHDPzHdqvd323o7JMw5bETF2', u'VUXysa3cnGeuIqTRWRCbsgljX062']]
listOfUsersBlue = [[u'YH7wXhrgkgM2ZeVwqoQ4kH1C87o1', u'bZtYnZv7IOUe9s6xXQ8eG74CsUr1', u'dOC7jFDcyPNtsVpRoqb3vm4QssJ2'],
                  [u'gJWkTZD9adZclSGez0Lw6ms4d3w2', u'ilk7QtgVjuR3VF35RWYiLTNex853', u'q6kLtZncQZcOgWQ2T9zRIUECqFk1'],
                  [u'vui79lCDT5NtzI4uGNb9M0N6q983', u'wIXqPpF1tlbbBmsnHElCn8lEgwm2', u'yESKrNoKcNZYOZ7cjFgbfcJ8QvL2']]

# for m in range(len(listOfUsersRed)):
#     for k in range(len(listOfUsersRed[m])):
#         # database.collection(u'users').document(listOfUsersRed[m][i]) \
#         #     .collection(u'tournaments').document(u'ISRD' + str(num)).set({
#         #
#         # })
#         database.collection(u'users').document(listOfUsersRed[m][k]) \
#             .collection(u'tournaments').document(u'PreSeason').set({
#
#         })
#
#         for i in range(len(json_obj)):
#             if str(json_obj[i][u'comp_level']) == (u'qm'):
#                 match_number = str(json_obj[i][u'match_number'])
#                 if int(match_number) < 10:
#                     match_number = u'0' + str(match_number)
#                 teamToScout = str(json_obj[i][u'alliances'][u'red'][u'team_keys'][m]).split(u'frc')
#                 database.collection(u'users').document(listOfUsersRed[m][k]) \
#                     .collection(u'tournaments').document(u'PreSeason').collection(u'gamesToScout') \
#                     .document(str(match_number)).set({
#                     u'teamNumber': teamToScout[1],
#                     u'saved': False,
#                     u'allianceColor': u'red'
#                 })

for m in range(len(listOfUsersBlue)):
    for k in range(len(listOfUsersBlue[m])):
        # database.collection(u'users').document(listOfUsersRed[m][i]) \
        #     .collection(u'tournaments').document(u'ISRD' + str(num)).set({
        #
        # })
        database.collection(u'users').document(listOfUsersBlue[m][k]) \
            .collection(u'tournaments').document(u'PreSeason').set({

        })

        for i in range(len(json_obj)):
            if str(json_obj[i][u'comp_level']) == (u'qm'):
                match_number = str(json_obj[i][u'match_number'])
                if int(match_number) < 10:
                    match_number = u'0' + str(match_number)
                teamToScout = str(json_obj[i][u'alliances'][u'blue'][u'team_keys'][m]).split(u'frc')
                database.collection(u'users').document(listOfUsersBlue[m][k]) \
                    .collection(u'tournaments').document(u'PreSeason').collection(u'gamesToScout') \
                    .document(str(match_number)).set({
                    u'teamNumber': teamToScout[1],
                    u'saved': False,
                    u'allianceColor': u'blue'
                })
