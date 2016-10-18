import pymongo


# gets you the handler on the mongo client
client = pymongo.MongoClient()
# choose the data base
db = client.Surveys
# choose the collection
collection = db.usersurveys
# example code


def insertRecords(username, email, surveyResponse):
    collection.insert({"username": username,
                       "email": email,
                       "color": surveyResponse['color'],
                       "food": surveyResponse['food'],
                       "vacation": surveyResponse['vacation'],
                       "fe-before": surveyResponse['fe-before'],
                       "fe-after": surveyResponse['fe-after']
                       })


def display():
    return collection
