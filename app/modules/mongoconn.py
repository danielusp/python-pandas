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

    return mycol.find()

#######################
#
# Normalize json format
# to DataFrame
#
#######################
def normalize_data(mongo_instance):
        normalized = json_normalize(list(mongo_instance))
        return pd.DataFrame(normalized)