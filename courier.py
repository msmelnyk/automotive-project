# add mongo driver
import config as cf
import json
import uuid
from pymongo import MongoClient


# db = client.test
# test = db.test


def get_mongo_connection():
    client = MongoClient(cf.db_creds['mongo_cluster'])
    prod = client.prod
    try:
        print(prod.command('find()'))

    except Exception as e:
        print(e)
    else:
        # log
        print('---Connect to DB: successful')

    return prod


def get_last_load_date_time(prod = get_mongo_connection()):
    return prod.history_0.find().sort({"ts":1}).limit(1)


def web_courier():
    mongo_cluster_history = get_mongo_connection()
    to_load = list()

    with open('data_for_test.json') as file:
        data = file.read()

    if len(data)
    # print('read rows: ' + str(len(data)))

    if isinstance(data, list) and data:
        for i in data:
            if i['cat'] > :
                to_load.append(i)



        print(
            test.insert_one({'_id': str(uuid.uuid4()),
                             'array': file_data,
                             'created_at': str(datetime.datetime.now())
                             }
                            )
        )
        print(str(datetime.datetime.now()))
        print(i)

    # print(len(file_data))

    # Inserting the loaded data in the Collection
    # if JSON contains data more than one entry
    # insert_many is used else insert_one is used
    for i in range(1, 20, 1):
        if isinstance(file_data, list):
            print(
                test.insert_one({'_id': str(uuid.uuid4()),
                                 'array': file_data,
                                 'created_at': str(datetime.datetime.now())
                                 }
                                )
            )
            print(str(datetime.datetime.now()))
            print(i)

    pass


def local_courier(data):
    try:
        if type(data) == dict:
            with open('local_storage.txt', 'a') as file:
                file.write(
                    str(
                        dict(id=uuid.uuid4(),
                             component_name='local_courier',
                             data=data,
                             error=0,
                             error_type='',
                             error_details=''
                             )
                    ) + '\n'
                )
        else:
            with open('logs.txt', 'a') as file:
                file.write(
                    str(
                        dict(id=uuid.uuid4(),
                             component_name='local_courier',
                             data=data,
                             error=1,
                             error_type='non dict value',
                             error_details=''
                             )
                    ) + '\n'
                )

    except Exception as e:
        with open('logs.txt', 'a') as file:
            file.write(
                str(
                    dict(id=uuid.uuid4(),
                         component_name='local_courier',
                         data=data,
                         error=1,
                         error_type='fatal error',
                         error_details=str(e)
                         )
                ) + '\n'
            )

            # with open('data.json') as file:
            #     file.write(json.dumps(dictionary, indent=1))
            #     file_data = json.load(file)

# def users(db):
#     pass
