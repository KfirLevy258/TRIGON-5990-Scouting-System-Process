import firebase_admin
from firebase_admin import credentials, firestore

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


cred = credentials.Certificate('./ServiceAccountKey.json',)
default_app = firebase_admin.initialize_app(cred)
database = firestore.client()

# teamNumber = raw_input('Enter team number: ')
# districtNumber = raw_input('Enter district number: ')
districtNumber = 3
teamNumber = 1574

teamData = database.collection(u'tournaments').document(u'ISRD' + str(districtNumber)).collection(u'teams')\
    .document(str(teamNumber)).get()

get_chassis_overall_strength(teamData)

