import datetime
import time
import uuid
import platform
from multiprocessing import Process
import pygetwindow as gw
from courier import courier


last_active_window = ''


def get_active_window_title():
    try:
        return gw.getActiveWindowTitle()
    except Exception as e:
        # print('err on get_active_window_title:' + str(e))
        with open('logs.txt', 'a', encoding="utf-8") as file:
            file.writelines(
                str(
                    dict(
                        id=str(uuid.uuid4()),
                        component_name='get_active_window_title',
                        error=1,
                        error_type='fatal error',
                        error_details=str(e),
                        created_at=str(datetime.datetime.now())
                    )
                ) + ',\n'
            )
        return 'Desktop'


def watcher():
    try:
        global last_active_window
        active_window_title = get_active_window_title()

        if active_window_title == last_active_window:
            pass
        elif active_window_title != last_active_window:
            # get time and write to file and reserve storage

            # print(str(datetime.datetime.now()) + ': { ' + last_active_window + ' - end}')
            # print(str(datetime.datetime.now()) + ': { ' + active_window_title + ' - start}')

            courier(
                dict(
                    datetime=str(datetime.datetime.now()),
                    last_active_window=last_active_window,
                    active_window_title=active_window_title,
                    username=platform.node()
                )
            )
            last_active_window = active_window_title

            # print('ok. watcher go')

        else:
            # print(
            #     str(datetime.datetime.now()) + '_2: { awt:' + active_window_title + ', law:' + last_active_window + '}')  ##################

            with open('logs.txt', 'a', encoding="utf-8") as file:
                file.writelines(
                    str(
                        dict(
                            id=str(uuid.uuid4()),
                            component_name='watcher',
                            data=str(
                                'last_active_window: ' + last_active_window +
                                ', active_window_title: ' + active_window_title +
                                ', username: ' + platform.node()),
                            error=1,
                            error_type='fatal error, else',
                            error_details='unhandled value in watcher',
                            created_at=str(datetime.datetime.now())
                        )
                    )
                )
            # marked: done.  log about unhandled case with all info.
    except Exception as e:
        output_log = str(
            dict(
                id=str(uuid.uuid4()),
                component_name='watcher',
                error=1,
                error_type='fatal error, exception',
                error_details=str(e),
                created_at=str(datetime.datetime.now())
            )
        )
        with open('logs.txt', 'a', encoding="utf-8") as file:
            file.writelines(output_log + ',\n')
        print(output_log)

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
