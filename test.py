import time, os, platform, uuid, json
from getmac import get_mac_address as gmac
import datetime

from pymongo import MongoClient

import config as cf
import pymongo

# arr = os.listdir( str(os.path.expanduser('~')) + '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')

# print(type(os.path.expanduser('~') + r'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\main.exe'))

#
# client = MongoClient('')
#
# db = client.test
# test = db.test
#
# try:
#     print(db.command('serverStatus'))
# except Exception as e:
#     print(e)
# else:
#     print('---Connect to DB: successful')

with open('data.json') as file:
    file_data = json.load(file)


# to_load = list()
#
#
# input = open('data1.json')
#
# data = json.load(input)
#
# if isinstance(data, list) and data:
#     for i in data:
#         if i['cat'] > '2023-01-02':
#             to_load.append(i)
# else: print('test empty success')

# print('read rows: ' + str(len(data)))

# print(to_load)

# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else insert_one is used
# if isinstance(file_data, list):
#     for i in file_data:
#             print(
#                 test.insert_one({'_id': str(uuid.uuid4()),
#                                  'array': file_data,
#                                  'created_at': str(datetime.datetime.now())
#                                  }
#                                 )
#            )
#             print(str(datetime.datetime.now()))
#             print(i)

# print(test.insert_many([{"i": i} for i in range(10000)]))


def get_mongo_connection():
    client = MongoClient(cf.db_creds['mongo_cluster'])
    test = client.test
    try:
        print(test.command('serverStatus'))

    except Exception as e:
        print(e)
    else:
        # log
        print('---Connect to DB: successful')

    return test


def get_last_load_date_time(test=get_mongo_connection(), data=list()):
    try:
        data = test.test.find().sort({"ts", pymongo.ASCENDING}).limit(1)
        # .find({}, {"created_at": 1, "_id": 0}).sort("_id", -1).limit(1)

    except Exception as e:
        print(e)
    else:
        # log
        print('---Connect to DB: successful')
    return data


print(get_last_load_date_time())
