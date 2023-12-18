import datetime
import uuid
import config as cf

from pymongo import MongoClient


def get_mongo_connection():
    try:
        db = MongoClient(cf.db_creds['mongo_cluster'])
        history = db.prod.history
        # print(history.count())
        db.prod.command('serverStatus')
    except Exception as e:
        output_log = str(
            dict(id=str(uuid.uuid4()),
                 component_name='get_mongo_connection',
                 data=None,
                 error=1,
                 error_type='fatal error',
                 error_details=str(e),
                 created_at=str(datetime.datetime.now())
                 )
        )
        with open('logs.txt', 'a', encoding="utf-8") as file:
            file.write(output_log + ',\n')
        print(output_log)
    else:
        # log
        print('---Connect to DB: successful')
    return history


def courier(data):
    try:
        if type(data) is dict:
            output = dict(
                id=str(uuid.uuid4()),
                component_name='courier',
                data=data,
                created_at=str(datetime.datetime.now())
            )

            with open('local_storage.txt', 'a', encoding="utf-8") as file:
                file.write(str(output) + ',\n')

            mongo_cluster_history = get_mongo_connection()

            # print(
            mongo_cluster_history.insert_one({
                '_id': str(uuid.uuid4()),
                'data': output
            })
            # )
            # print(str(datetime.datetime.now()))
            # print(data)

            with open('logs.txt', 'a', encoding="utf-8") as file:
                file.write(
                    str(
                        dict(id=str(uuid.uuid4()),
                             component_name='local_courier',
                             data=output,
                             error=0,
                             error_type=None,
                             error_details='successful write new record to storages',
                             created_at=str(datetime.datetime.now())
                             )
                    ) + ',\n'
                )
            print('successful write new record to storages')

        else:
            output_log = (
                str(
                    dict(id=str(uuid.uuid4()),
                         component_name='local_courier',
                         data=data,
                         error=1,
                         error_type='error on input from watcher',
                         error_details='exist not dict value',
                         created_at=str(datetime.datetime.now())
                         )
                )
            )
            with open('logs.txt', 'a', encoding="utf-8") as file:
                file.write(output_log + ',\n')
            print(output_log)

    except Exception as e:
        output_log = (
            str(
                dict(id=str(uuid.uuid4()),
                     component_name='courier',
                     messege='except error in courier',
                     data=data,
                     error=1,
                     error_type='exception',
                     error_details=str(e),
                     created_at=str(datetime.datetime.now())
                     )
            )
        )

        with open('logs.txt', 'a', encoding="utf-8") as file:
            file.write(output_log + ',\n')
        print(output_log)
