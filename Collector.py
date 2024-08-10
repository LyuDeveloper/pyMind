import os
from Mind import *
import datetime

logDir = 'Collector'
log("pyMind Data Collector", logDir)

global operating_data_json
global DataInDirNum

DataFileList = json_files()
log("checking json data", logDir)
FileInDir = os.listdir("./Data/")
today = datetime.date.today()


def data_remover():
    for j in DataFileList:
        os.remove(f"./Data/{j}")
    with open(f"./Data/1.json", mode="a", encoding="utf-8"):
        pass

def init():
    global DataInDirNum
    global operating_data_json
    DataInDirNum = 0
    for i in DataFileList:
        if i in FileInDir:
            DataInDirNum += 1
        else:
            with open(f"./Data/{i}", mode="a", encoding="utf-8"):
                log(f'Can\'t find {i} .Creating it.', logDir)
                operating_data_json = i
            break
        if DataInDirNum == len(DataFileList):
            log('Datas collected. Starting Mind...', logDir)
            Mind()
            log('Datas have already created. Removing them...', logDir)
            data_remover()
            operating_data_json = '1.json'

init()


def data_encoder(device, kind, timer = datetime.datetime.now().strftime("%H:%M:%S")):
    # device:Operated devices
    # kind:Types of devices being operated on
    # timer:The time when the operation occurred (default current time, used for debugging)
    global operating_data_json

    if datetime.date.today() != today:
        init()

    log(f'New Operation. Device:{device}, Kind:{kind}, Time:{timer}. Writing {operating_data_json}', logDir)
    data = json.dumps({'Device': device, 'Kind': kind, 'Time': timer}, sort_keys=True, indent=4, separators=(',', ': '))
    make_json(data, f"./Data/{operating_data_json}")
