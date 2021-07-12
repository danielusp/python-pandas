import pandas as pd
import pymongo
from pandas.io.json import json_normalize

#######################
#
# Conect mongo db
#
#######################
def mongo(db, collection):
    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    mydb = myclient[db]
    mycol = mydb[collection]

    return mycol

#######################
#
# Normalize json format
# to DataFrame
#
#######################
def normalize_data(mongo_instance):
        mongo_instance = mongo_instance.find()
        normalized = json_normalize(list(mongo_instance))
        return pd.DataFrame(normalized)


#######################
#
# Apply a aggregate query
# to a Mongo instance
#
#######################
def aggregate(mongo_instance, pipeline):
    #Make empty dataframe
    df = pd.DataFrame()

    #add each doc as a new row in dataframe
    for doc in mongo_instance.aggregate(pipeline):
        df = df.append(doc, ignore_index=True)
    
    return df
