import datetime


def json_files():
    data_file_list = ['1.json', '2.json', '3.json', '4.json', '5.json', '6.json', '7.json']
    return data_file_list


def log(context, log_dir):
    now_datetime = datetime.date.today()
    context = str(context)
    with open(f"./Log/{log_dir}/{str(now_datetime)}.log", mode="a", encoding="utf-8") as logFile:
        logFile.write('[' + str(datetime.datetime.now()) + '] ' + context + '\n')
        print('[' + str(datetime.datetime.now()) + '] ' + context)


def make_json(data, json_dir):
    context_result = '['
    with open(json_dir, mode="r+", encoding="utf-8") as Json_File:
        context = Json_File.read()
        for k in context:
            if len(context_result) != len(context) - 1 and k != '[' and k != ']':
                context_result += k
        if context == '':
            context_result = context_result + data + '\n]'
        else:
            context_result = context_result + ',' + data + '\n]'
    with open(json_dir, mode="w+", encoding="utf-8") as Json_File:
        Json_File.write(context_result)
