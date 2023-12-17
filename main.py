import datetime
import os
import time
import uuid
import platform
from getmac import get_mac_address as gmac
from multiprocessing import Process
import pygetwindow as gw
import config as cf
from courier import local_courier
from pymongo import MongoClient

last_active_window = ''


def get_active_window_title():
    # to do: read the docs about this func
    try:
        # active_window = gw.getActiveWindow()
        # active_wt = gw.getActiveWindowTitle()
        # print(active_window)
        # print(str(active_wt))
        # print(str(active_window.title))
        # return active_window.title
        return gw.getActiveWindowTitle()
    except Exception as e:
        print('E:' + str(e))

        with open('logs.txt', 'a') as file:
            file.writelines(
                str(
                    dict(id=uuid.uuid4(),
                         component_name='get_active_window_title',
                         error=1,
                         error_type='fatal error',
                         error_details=str(e)
                         )
                ) + '\n'
            )
        return 'None'


# sneaker





def watcher():
    global last_active_window
    active_window_title = get_active_window_title()

    if active_window_title == last_active_window:
        pass
    elif active_window_title != last_active_window:
        # get time and write to file and reserve storage

        print(str(datetime.datetime.now()) + ': { ' + last_active_window + ' - end}')
        print(str(datetime.datetime.now()) + ': { ' + active_window_title + ' - start}')

        local_courier(
            dict(
                datetime=str(datetime.datetime.now()),
                last_active_window=last_active_window,
                active_window_title=active_window_title,
                mac=gmac(),
                username=platform.node()
            )
        )
        # print(str(datetime.datetime.now()) + '_1: { awt:' + active_window_title + ', law:' + last_active_window + '}')
        last_active_window = active_window_title
    else:
        print(str(datetime.datetime.now()) + '_2: { awt:' + active_window_title + ', law:' + last_active_window + '}')
        # log about unhandled case with all info. if exist that, call me in chanel for this in evening every day.


# def job():
#     print(str(datetime.now()) + " Schedule start..")
#     logging_service(str(datetime.now()) + " Start schedule", "SCHEDULE", 200)


def wait():
    # schedule.every().day.at("09:30").do(job)
    print('Subprocess started')
    while True:
        # schedule.run_pending()
        watcher()
        time.sleep(2)


if __name__ == '__main__':
    print("Main started")
    p = Process(target=wait)
    p.start()

# q: infinity loop with sleep, 2 seconds? maybe longer or shorter?
# to do: write file module and calls it "courier"
# to do: write checker for changes in active window and calls it "watcher"
# to do: write logger
# to do: write scheduler for all of it

# try:
#     active_window_title = get_active_window_title()
#     if active_window_title and :
#         last_active_window.append(active_window_title)
#         print("Active Window Title:", active_window_title)
#     else:
#         print("No active window found.")
# except Exception as e:
#     print(e)
