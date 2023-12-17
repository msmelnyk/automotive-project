import time
import os
import shutil

fid = os.listdir(str(os.path.expanduser('~')) + r'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')

try:
    fid.index('main.exe')
    with open('logs.txt', 'a') as file:
        file.writelines(str(time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())) +
                        ', SUCCESS\n'
                        )
except ValueError:
    with open('logs.txt', 'a') as file:
        file.writelines(str(time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())) +
                        ', cwd: ' + str(os.getcwd()) + '\n'
                        )
        file.writelines(str(time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())) +
                        ', expanduser: ' + str(os.path.expanduser('~')) + '\n'
                        )

    source = os.getcwd() + r'\main.exe'

    # Destination path
    destination = str()

    try:
        dest = shutil.copyfile(os.getcwd() + r'\main.exe',
                               os.path.expanduser('~') + r'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\main.exe')
        with open('logs.txt', 'a') as file:
            file.writelines(str(time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())) +
                            ', destination result: ' + str(dest) + '\n'
                            )
    except Exception as e:
        with open('logs.txt', 'a') as file:
            file.writelines(str(time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())) +
                            ', err: ' + str(e) + '\n'
                            )
